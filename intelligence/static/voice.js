'use strict';
// Dictation is a draft: only explicit insertion changes the comment field.
function attachCommentVoice({Recognition,button,insert,discard,status,preview,field,save}) {
  let recognizer=null,active=false,draft='',interim='',timer=null,disposed=false,error='';
  function paint(){
    button.textContent=active?'Stop dictation':'Dictate comment';
    button.setAttribute('aria-pressed',String(active));
    preview.textContent=[draft,interim].filter(Boolean).join(' ');
    insert.disabled=active||!draft;discard.disabled=active||!draft;
    save.disabled=active||!!draft;
  }
  function finish(){active=false;clearTimeout(timer);recognizer=null;interim='';paint();status.textContent=error||(draft?'Review the transcript, then add it to your comment or discard it.':'No speech captured. Try again or type your comment.');}
  function dispose(){disposed=true;clearTimeout(timer);if(recognizer){recognizer.onresult=recognizer.onerror=recognizer.onend=null;try{recognizer.abort();}catch(e){}}recognizer=null;}
  button.onclick=()=>{
    if(active){button.disabled=true;status.textContent='Finishing transcript…';try{recognizer.stop();}catch(e){finish();button.disabled=false;}return;}
    error='';interim='';
    try{
      recognizer=new Recognition();recognizer.lang='en-US';recognizer.continuous=true;recognizer.interimResults=true;
      recognizer.onresult=e=>{if(disposed)return;interim='';for(let i=e.resultIndex;i<e.results.length;i++){const r=e.results[i];if(r.isFinal)draft+=(draft?' ':'')+r[0].transcript.trim();else interim+=(interim?' ':'')+r[0].transcript;}paint();};
      recognizer.onerror=e=>{if(disposed)return;error=({ 'not-allowed':'Microphone access was denied. Allow it in your browser settings or use keyboard dictation.', 'service-not-allowed':'Speech recognition is unavailable here. Use keyboard dictation or open the desk in a supported browser.', 'audio-capture':'No microphone is available. Connect one or type your comment.', 'network':'The speech service could not connect. Your captured text is preserved.', 'no-speech':'No speech detected. Try again or type your comment.' })[e.error]||'Dictation stopped. Review any captured text or try keyboard dictation.';status.textContent=error;try{recognizer.stop();}catch(x){};};
      recognizer.onend=()=>{if(disposed)return;button.disabled=false;finish();};
      active=true;paint();status.textContent='Listening… Speak your feedback. Stops automatically after 60 seconds.';recognizer.start();
      timer=setTimeout(()=>{if(active&&recognizer){status.textContent='Time limit reached. Finishing transcript…';recognizer.stop();}},60000);
    }catch(e){error='Speech recognition could not start here. Use your device’s keyboard dictation or type.';if(recognizer){try{recognizer.abort();}catch(x){}}button.disabled=false;finish();}
  };
  insert.onclick=()=>{const merged=field.value+(field.value.trim()?'\n':'')+draft;if(merged.length>field.maxLength){status.textContent='This transcript exceeds the comment limit. Shorten your existing comment or discard and dictate a shorter note. Nothing has been removed.';return;}field.value=merged;field.dispatchEvent(new Event('input',{bubbles:true}));draft='';paint();status.textContent='Transcript added. Edit your comment, then Save comment.';field.focus();};
  discard.onclick=()=>{draft='';interim='';paint();status.textContent='Transcript discarded. Your existing comment is unchanged.';};
  if(!Recognition){button.disabled=true;status.textContent='Browser dictation is unavailable here. Click the comment field and use your device’s keyboard dictation, or open this desk in a browser with speech recognition.';}
  paint();return dispose;
}
