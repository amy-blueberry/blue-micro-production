const assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
let instance;
class Recognition{constructor(){instance=this;}start(){}stop(){this.onend?.();}abort(){this.aborted=true;}}
const context={Event:class{},setTimeout:()=>1,clearTimeout(){}};vm.createContext(context);vm.runInContext(fs.readFileSync('intelligence/static/voice.js','utf8'),context);
function el(){return {textContent:'',value:'Existing note',maxLength:2000,disabled:false,setAttribute(){},dispatchEvent(){},focus(){}};}
function setup(R=Recognition){const x={Recognition:R,button:el(),insert:el(),discard:el(),status:el(),preview:el(),field:el(),save:el()};x.dispose=context.attachCommentVoice(x);return x;}
let x=setup();x.button.onclick();assert(x.save.disabled);instance.onresult({resultIndex:0,results:[Object.assign([{transcript:'Explain the character choice.'}],{isFinal:true})]});assert.equal(x.field.value,'Existing note');x.button.onclick();assert(x.save.disabled);x.insert.onclick();assert.equal(x.field.value,'Existing note\nExplain the character choice.');assert(!x.save.disabled);
x=setup();x.button.onclick();instance.onresult({resultIndex:0,results:[Object.assign([{transcript:'Temporary'}],{isFinal:false})]});x.button.onclick();assert.equal(x.preview.textContent,'');assert(!x.save.disabled);
x=setup();x.button.onclick();instance.onresult({resultIndex:0,results:[Object.assign([{transcript:'Long text'}],{isFinal:true})]});x.button.onclick();x.field.maxLength=5;x.insert.onclick();assert.equal(x.field.value,'Existing note');assert(x.save.disabled);x.discard.onclick();assert(!x.save.disabled);
x=setup();x.button.onclick();instance.onerror({error:'not-allowed'});assert.match(x.status.textContent,/denied/);assert(!x.save.disabled);
x=setup();x.button.onclick();const old=instance;x.dispose();assert(old.aborted);assert.equal(old.onresult,null);
x=setup(null);assert(x.button.disabled);assert.match(x.status.textContent,/keyboard dictation/);
console.log('6 voice interaction checks passed');
const grouped=context.suggestFeedbackSections('The observations are correct. The interpretation is generic. Make the next step specific. More emotional detail please.');
assert.equal(grouped.length,4);assert.equal(grouped[0].section,'observed');assert.equal(grouped[1].section,'meaning');assert.equal(grouped[2].section,'next_step');assert.equal(grouped[3].section,'general');
assert.equal(context.suggestFeedbackSections('The observations and interpretation disagree.')[0].section,'general');
assert.equal(grouped.map(r=>r.text).join(' '),'The observations are correct. The interpretation is generic. Make the next step specific. More emotional detail please.');
console.log('Whole-brief assignment checks passed');
