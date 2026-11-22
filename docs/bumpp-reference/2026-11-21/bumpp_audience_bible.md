# bumpp Audience Intelligence Bible
### Who watches stories filmed inside Roblox and Minecraft, and how to write for them

November 21, 2026 · Internal / Confidential

Owner: Blueberry Entertainment Inc. (bumpp)

Purpose: the audience reference for bumpp's script-writing engine. It describes the five cohorts we write for in depth, so the engine can write for each one and test finished shows against all of them.

---

## 1. What this file is for

This document gives bumpp's script-writing engine a complete working understanding of the five audience cohorts we write for. It has two jobs:

1. **Write for a cohort.** Develop shows, characters, scripts, and dialogue that a specific cohort will choose, follow, and come back to.
2. **Test a finished show against the cohorts.** Score a completed show against every cohort and predict which ones it will resonate with, where it breaks, and what to fix.

Everything else in the file (market data, culture, voice, craft, safety) exists to make those two jobs accurate.

### 1.1 How to use this file

**Mode A: writing a show**

1. Read Section 2 (the audience at a glance) and pick exactly one primary cohort using Section 2.3.
2. Read that cohort's full dossier (Sections 3 to 7): the cohort card, personas, what they watch and play, what they want to feel, tropes, characters, voice, dialogue bank, format, and resonance scorecard.
3. Read Section 8 (voice and language), Section 9 (culture), and Section 10 (story craft) for the shared rules.
4. Fill in the Development brief (Section 13.5) before writing a premise, then use the template and prompt in Section 13.
5. Before handing anything over, score your own draft against the cohort's scorecard (Section 14) and fix anything below 14 of 20.

**Mode B: testing a finished show**

1. Run the Resonance test in Section 14.
2. Score the show against all five cohort scorecards (Sections 3.14, 4.14, 5.14, 6.13, 7.9) and the universal craft criteria (14.4).
3. Return the resonance matrix, the primary verdict, and prioritized revisions in the format in 14.8.

**What never changes:** the safety rules in Section 12 and the non-negotiables in 1.3 apply in both modes.

**Appendices** hold the market evidence, the research plan, and the sources. The engine can consult them but does not need them to write.

### 1.2 Evidence tags
Every factual claim carries a tag. The engine should weight claims by tag and never present an [I] item as fact in pitch materials.

| Tag | Meaning |
|---|---|
| **[D]** | Data. Published survey, company filing, or third-party measurement. Source listed in Appendix C. |
| **[O]** | Observed. Pulled directly from creator channels, video titles, view counts, captions, or fan posts in Nov 2026. Real, but a sample, not a census. |
| **[K]** | Known context from before mid-2026 that was not re-verified for this file. Re-check before external use. |
| **[I]** | Inference or hypothesis. Our reasoning from the data. Test it with real performance data before treating it as settled. |
| **[NS]** | From the internal bumpp North Star (May 2026). Company position, not external data. |
| **[P]** | From a parallel research pass (Nov 21, 2026) with its own linked sources. Included because it is useful; we did not independently re-verify every figure. Re-check before external use. |

### 1.3 Non-negotiables for anything the engine generates

1. All content is for viewers 13 and older and is designed for 16+. Nothing is ever child-directed (Section 2.1). The audience still includes minors, and so do many characters. Characters who are minors are never sexualized, in dialogue, framing, wardrobe direction, or camera direction. Romance between minor characters stays at crush, longing, jealousy, hand-holding, and an off-screen or implied kiss at most. See Section 12.
2. Characters speak the audience's language. The brand voice does not. Slang lives in character mouths, scaled to who the character is (Section 8).
3. Adapt tropes, not titles. Do not reproduce copyrighted shows, songs, lyrics, or named characters (Section 12).
4. Every show must clear the screenshot test, the group-chat test, and the episode-2 test (Section 10).

---

## 2. The audience at a glance

### 2.1 Who we write for: age floor and target (company decision)

| | Ages | What it means for the engine |
|---|---|---|
| **Floor** | 13+ | Nothing is child-directed. No content, packaging, thumbnails, or titles that read as made for children under 13. |
| **Design target (core)** | 16 to 19 | Every show must work first for this viewer. |
| **Ascending** | 20 to 24 | Higher spend; college, work, and adult-life stories. |
| **Spillover** | 13 to 15 | Will watch because teens watch up. Not a design target. A safety constraint. |
| **Characters** | 17 to 21 by default | Senior year, gap year, college, first jobs, moving out. Romance-led shows default to leads who are 18+. |

**Why older** [D][I]

- Roblox moves users from Roblox Select to standard accounts at 16, so a 16+ viewer can follow a show into any companion map or event.
- Users 18+ are Roblox's fastest-growing segment and monetize 50%+ more than under-18s.
- It matches the North Star's 16 to 22 ICP and makes the "A24 meets K-drama" register credible.
- It positions every channel clearly as teen- and young-adult-directed, which supports keeping comments and community features on YouTube. (COPPA "made for kids" turns on under-13 direction; 13+ positioning already avoids it, and 16+ makes it unambiguous. Counsel should confirm.)

**What it costs** [O][I]

- The most intense Roblox-drama fans today are 13 to 15. We trade some raw fandom energy for spend and creative range.
- At 16 to 24 we compete with K-dramas, prestige teen TV, and microdrama apps, so production quality has to carry more weight.

### 2.2 The five cohorts

Five concentric cohorts, ordered by how likely they are to resonate with drama, horror, and serialized stories filmed inside games. Cohort 1 is the bullseye. Each cohort outward is larger, less committed, and needs a stronger hook.

| Cohort | Name | Ages (core) | Gender skew | Relationship to the format | Est. reach | Primary genres |
|---|---|---|---|---|---|---|
| 1 | **The Lore Keepers** | 15 to 19 | Strongly female | Already watch Roblox series; audition, edit, theorize | Smallest, most valuable | Academy drama, romance, rivalry, glow-up, mystery |
| 2 | **The Drama Girls** | 16 to 22 | Strongly female | Watch K-dramas, teen TV, BookTok, microdrama clips; play DTI and Royal High; don't yet watch Roblox series | Large | Romance, revenge, fantasy royalty, friendship drama |
| 3 | **The Scream Team** | 15 to 21 | Mixed, slight male | Play Roblox horror, watch lore and theory content, went to Backrooms in a group | Large | Horror, mystery, survival, sci-fi, thriller |
| 4 | **The Lobby** | 15 to 21 | Male-leaning | Play everything; watch gaming YouTube, brainrot, anime; Minecraft SMP lore | Largest in-platform | Comedy, action, competition, lore, anime-style fantasy |
| 5 | **The Crossover** | 18 to 24 | Mixed | College-age players, lapsed players, microdrama-app viewers, international young adults | Large, high spend | College and workplace drama, reality, satire, nostalgia, prestige horror |

Each cohort has a full dossier in Sections 3 to 7, built in the same order so the engine can compare them field by field: cohort card, snapshot, personas, behaviors, media diet, emotional jobs, tropes, characters, voice, cringe triggers, what wins them, format, deepening, dialogue bank, and resonance scorecard. With the 16+ target, Cohorts 2 and 5 move from the edge toward the center of the slate, and Cohort 1 is served through its older members (16 to 19).

### 2.3 One primary cohort per show, and how to choose between neighbors [P][I]
Every show has exactly one primary cohort: the pleasure its creators promise and will protect when two choices conflict. A secondary cohort can get an adaptation as long as the primary audience's reason to return stays intact.

| Cohort | The viewer's reason to choose another part | The distinction that changes the writing |
|---|---|---|
| Lore Keepers | "I know what that meant between those two." | Accumulated relationship history changes the meaning of a present action. Give the best friend a continuing life. |
| Drama Girls | "I need to see which one will actually choose the other." | Familiar relationship tension can pull them past unfamiliar avatars. Earn a reversal through agency on both sides. |
| Scream Team | "I saw it change. Who else knows?" | An observable rule gives fear, prediction, and release, alone or as a group. |
| The Lobby | "That's our teammate. I want to see how they get out of this." | A legible challenge or joke opens the door; a choice with a social cost makes watching worth time away from play. |
| The Crossover | "My roommate would watch this even if I never mentioned Roblox." | A genre or real-life stake must work for a newcomer on first contact. |

**Choosing between neighbors.** A mystery about a missing teammate is Lore Keepers if a prior friendship makes a witness's omission hurt, Scream Team if working out the rule is the main pleasure, and The Lobby if the group must decide who gives up the winning position. For a relationship premise: if knowing this particular cast is the draw, it's Lore Keepers; if people will cross from another medium for the pairing or trope, it's Drama Girls. If it survives mainly on a recognizable dilemma and a friend's recommendation, it's The Crossover.

**The tiebreaker question:** name the one payoff the show would protect if the runtime were cut in half.

**Viewing-habit tags** (record alongside the cohort, no numbers): returning Roblox-series viewer · Minecraft or other serialized-world viewer · primarily a player · clip-first viewer · genre-first newcomer. "Scream Team · Minecraft-first · watches with a cousin" tells writers more than a demographic label.

### 2.4 The ten truths about this audience

1. **The core viewer is a teen girl who already follows long-form drama made inside games.** The genre exists, has stars, has studios, and has fandoms. We are entering a scene, not inventing one. Under the 16+ target she may watch more than she plays: girls' gaming drops off after 14 (Appendix A1.7). [O][D]
2. **We design for 16 to 19, ascend to 20 to 24, and accept 13 to 15 as spillover.** The existing Roblox-drama fandom skews 13 to 17, but bumpp deliberately aims one step older: it aligns with Roblox's 16+ standard accounts, the North Star's 16 to 22 ICP, and the higher-spending 18+ segment. See Sections 2.1 and A1.4. [D][O][I][NS]
3. **Episode one is the show, and the return is the goal.** Across every studio sampled, episode one has 3x to 7x the public views of later episodes. Public totals are not same-viewer retention (Appendix A2.5), but the pattern says the hard problem is getting someone to choose part two. Resonance means a voluntary return (Appendix A3.1). [O][P]
4. **The cast is the franchise.** Studios run podcasts, cast Q&As, "Sip or Spill" interviews, cooking videos with the cast, and public auditions. Fans follow the actors (the players behind the avatars) as much as the characters. [O]
5. **Friendship carries as much weight as romance.** In the 2026 UCLA Teens and Screens survey, 57.3% want more platonic relationships on screen and "friendships and social groups" ranked as the #2 thing they want to see. Romance hooks; friendship retains. [D]
6. **Hope beats nihilism.** The #1 request in the same survey: "hopeful, uplifting stories with people beating the odds." Partying, drugs, and drinking ranked last. Dark is fine. Bleak is not. [D]
7. **Horror is a co-equal pillar, not a side genre.** Young YouTube-native horror (Backrooms, Obsession) owned the 2026 box office with audiences mostly under 25, and survival-horror games sit in Roblox's top 10. [D]
8. **Fashion is plot.** Avatars, outfits, and "how to get this look" tutorials are content in their own right. This is where Blueberry's catalog connects to the shows. [O][I]
9. **International is the majority.** APAC alone has about 1.75x the Roblox daily users of the US and Canada (42M vs 24M in Q3 2026), and roughly five in six users are outside US/Canada. Write stories that travel; avoid plots that only work in an American high school. [D]
10. **Cringe is fatal and fast.** Gen Alpha publicly "reset" its meme vocabulary on January 1, 2026. Dated slang, adult-coded "hey besties" energy, and trying-too-hard captions lose this audience on frame one. [D][NS]

### 2.5 Key numbers to keep in mind

- Roblox had 138 million daily users in Q3 2026; age-checked users split 34% under 13, 37% aged 13 to 17, 29% aged 18 and over. Adults are the fastest-growing group. [D]
- About 30% of US 13 to 17 year olds use Roblox daily; 49% of US teens use it at all. [D]
- Daily users by region: APAC 42M, Rest of World 40M, Europe 32M, US and Canada 24M. US and Canada still produce over half of revenue. [D]
- Girls' gaming drops with age: 81% of US girls aged 13 to 14 play video games vs 67% at 15 to 17, and only 17% of teen girls call themselves gamers. The 16+ girl is often reached through drama habits, not play. [D]
- In the US, female weekly Roblox mobile users passed male users in 2026. [D]
- YouTube and Netflix are tied for teens' daily video time; TikTok is teens' favorite app. [D]
- 35% of Gen Z (13 to 24) watch microdramas; the format's audience is getting younger and more male. [D]
- Young viewers most want "hopeful, uplifting stories with people beating the odds," friendships, and lives like theirs; 57% want more platonic relationships on screen. [D]
- YouTube-made horror (*Backrooms*, *Obsession*) owned the 2026 box office with audiences mostly under 25. [D]
- In the reference Roblox series, Episode 1 draws roughly 3x to 7x the public views of later episodes. Getting a viewer to choose part two is the central problem. [O]

Full data: Appendices A1 to A3. Sources: Appendix C.

### 2.6 Internal context (bumpp North Star)

From the bumpp North Star (May 2026) and Brand Supplement v4 (June 2026). The engine should treat these as the company's standing creative position. [NS]

- **What bumpp is:** "Netflix for the Roblox audience." Original shows set inside game worlds the audience already lives in (Royal High, Dress to Impress, Brookhaven, Bloxburg, Berry Avenue), plus Boopp, a companion character.
- **Core ICP in the North Star:** female-skewing, gaming-native, 16 to 22 at the heart, extending from 14 to 24.
- **Benchmark:** "A24 meets K-drama meets Royal High." Emotional realism, character interiority, atmospheric production, stories built to be edited and re-shared.
- **Slate mix in the North Star:** 50% elevated vertical drama, 30% prestige adaptation, 20% pure-format vertical drama.
- **Not:** ReelShort or DramaBox cheap billionaire-romance energy; Twitch or esports hype; kids'-app visuals; sex or violence as the hook.
- **Voice rule:** lowercase, short, understated. Never "hey besties" or "slay." Gamer language only in interface micro-copy.

> **Decision on age:** The North Star targets 16 to 22. The Roblox-native drama audience observed in this research skews younger, roughly 13 to 17, and the creators themselves are teenagers (the creator of Walden Academy describes herself as 17). Leadership has chosen to aim older: core viewers 16 to 19, ascending viewers 20 to 24, characters 17 to 21. The younger fandom will still find us; we do not design for it.

---

## 3. Cohort 1: The Lore Keepers
*"It's not a Roblox video. It's a series."*

### 3.0 Cohort card: Lore Keepers

| Field | Profile |
|---|---|
| Who | Viewers who follow a specific *cast* across episodes of a game-filmed series and return because of what is happening between particular characters |
| Ages | Fandom runs 13 to 17; bumpp writes for its older half, 15 to 19, center 17 |
| Gender | Strongly female; includes boys and nonbinary fans with the same return habit |
| Where | US first; heavy participation from the UK, Canada, Australia, the Philippines, and English-speaking Southeast Asia |
| Route in | Already watch Roblox series (or follow Minecraft and other serialized game worlds) |
| Reason to come back | "I know what that meant between those two." |
| What they want to feel | Knowing someone well enough to spot a lie; belonging to the group that remembers why it matters; room to change sides |
| Best genres | Elite academy and status drama, friendship mystery, slow-burn rivalry, found family, competition for a place in a group |
| Top tropes | Scholarship outsider, enemies to lovers, rival families, the anonymous account, the clique that cracks, the secret job |
| Register | Fast, ironic, layered, texting-native, fandom vocabulary; light to medium slang |
| Format | 12 to 25 minute ensemble episodes or linked chapters, with 60 to 90 second cutdowns of one debatable choice |
| What loses them | A friendship reset with no cost, a reveal with no earlier clue, characters switching sides because the plot needs it, everyone agreeing who is wrong |
| Signature test | A later choice whose cost depends on having seen an earlier moment of ordinary affection |

### 3.1 Snapshot

- **Ages:** the fandom runs 13 to 17; bumpp targets its older half, 15 to 19, center 17. [I from creator ages, fan framing, Roblox age data]
- **Gender:** strongly female; a meaningful minority of boys who act in or edit for studios. [O]
- **Geography:** US-led for the English-language studios, with heavy participation from the UK, Canada, Australia, the Philippines, and Southeast Asia (English-speaking players). [I]
- **Size proxy:** the top series pull 280K to 1.5M views per episode; prestige-tier studios hold 10K to 165K subscribers. This is a tight, intense, reachable community. [O]

### 3.2 Who she is (composite persona) [I]
**Kiera, 17, senior, suburban Texas (could as easily be Manila or Manchester).** She has watched every Walden Academy episode on release night and rewatched Episode 1 twice. She is in three studio Discords and auditioned for background roles in one. She runs a fan edit account with a few thousand followers, cuts clips in CapCut to songs she finds on TikTok, and posts prediction threads. She ships Romaire and will argue about it in the comments. She plays Berry Avenue to scout outfits and practice poses, Dress to Impress with her friends, and Royal High when she wants to feel pretty. Her phone goes in a pouch at school now; she makes up for it between 3:30 and midnight. She cried at a show finale this year and told her group chat about it. She would rather be cast as an extra in a show she loves than be famous for something she doesn't.

### 3.3 Behaviors that define the cohort [O]

- **Release-night ritual:** watches premieres live, comments in real time, then debriefs in Discord.
- **Theory and prediction culture:** text-post predictions, "explanation" threads, Pinterest boards per series.
- **Edit culture:** clips re-cut to music, couple edits, "character as aesthetic" edits.
- **Participation:** auditions via TikTok hashtag, background-actor sign-ups, voice-acting tryouts, behind-the-scenes Discord roles.
- **Cast fandom:** follows the players behind the avatars; watches cast Q&As and "Sip or Spill" interviews.
- **Utility content:** watches tutorials on dynamic heads, outfit recreation, and posing.

### 3.4 What she watches beyond Roblox [D][I]

- **TV/film:** Wednesday, Stranger Things (finale year), KPop Demon Hunters (rewatched repeatedly), Euphoria (aspirational, often watched against parental wishes), Heartstopper, Gossip Girl (rediscovered), Maxton Hall-type academy romance, The Summer I Turned Pretty-style love triangles. [D for Wednesday, Stranger Things, KPDH as Gen Z favorites; I for the rest]
- **K-culture:** K-drama clips and edits more than full episodes at 13 to 15; full binges by 16 to 17. KPop Demon Hunters is the gateway for many. [I]
- **Reading:** BookTok and Wattpad romance and romantasy, "swoon without the spice" at the younger end. [D]
- **YouTube:** Roblox series, Roblox Shorts stories, beauty and "get ready with me," commentary on fandom drama.

### 3.5 Emotional jobs the shows do for her [I]

| Job | What it sounds like in her head |
|---|---|
| Belonging | "My server is waiting to talk about this." |
| Status rehearsal | "What would I do if I were the scholarship girl?" |
| Safe intensity | Feel heartbreak, jealousy, betrayal without real-life cost |
| Identity play | Try on the queen bee, the outsider, the redemption arc |
| Creative fuel | Every episode is raw material for her own edits and theories |
| Proximity to creators | The stars are kids like her; she could be next |

### 3.6 Genres and tropes that hit (ranked by observed pull) [O][I]

1. **Elite academy / boarding school** with a scholarship or outsider lead.
2. **Enemies to lovers** and **rivals to lovers**, slow burn.
3. **Glow-up revenge:** humiliated, transformed, triumphant.
4. **Rich family feuds** and secret inheritances (*Vendetta*).
5. **Royalty and commoner** (Royal Assistant).
6. **Love triangle** with a "safe" option and a "dangerous" option.
7. **Found family / friend group under pressure:** the clique that might break.
8. **Secret identity / double life** (the scholarship girl hiding where she lives; the popular girl hiding a family crisis).
9. **Competition frame** (modeling, cheer, talent, fashion).
10. **Whodunnit inside the drama:** an anonymous account, a leaked list, a disappearance.

### 3.7 Characters she loves [I]

- **The morally gray girlboss** she's not supposed to like (Blaire-type). Fans write "she is pmo but icl she ate with this line." [O, caption paraphrased from a real fan post]
- **The cold rich boy who is soft for one person only.**
- **The loyal best friend who deserves her own storyline** (fans campaign for side characters).
- **The outsider with a moral spine** who refuses to become them.
- **The villain with a sympathetic wound** revealed late.

### 3.8 How she talks (register for Cohort 1 characters)
Use sparingly and only in character. Mix one or two markers per exchange, never a pile-up.

- Texting style: lowercase, minimal punctuation, abbreviations. "icl" (I can't lie), "ngl," "fr," "istg," "lowkey," "pmo" (pisses me off), "ts" (this), "be so fr," "the way she…," "not me…," "she ate," "she's her," "it's giving," "delulu," "pick me," "situationship," "crash out." [D][O]
- Spoken style: fast, ironic, layered. A compliment can be an insult and vice versa.

Sample lines (original, for register only):
> "not you acting brand new because you sat at their table once."
>
> "she's being so pick me right now and icl it's working."
>
> "if he texts back in under a minute i'm crashing out."
>
> "you don't get to be mysterious, you have a group chat with your mom."

### 3.9 Cringe triggers for Cohort 1 [I][NS]

- Adults performing teen slang ("slay, bestie!"). 
- Slang used in narration or on-screen captions by the "show" rather than characters.
- Plot holes she can screenshot. She will.
- Characters who change personality to serve the plot.
- Cheap avatars, bad lip sync to emotion, flat sound.
- Moralizing PSAs. Stories about phones being bad.
- Long gaps between episodes with no communication.

### 3.10 What wins her [I]

- **A ship and a rivalry in Episode 1,** with names she can hashtag.
- **A mystery that rewards rewatching** (clues placed for theorists).
- **Release cadence she can plan around** (same day, same time).
- **Ways in:** auditions, extras, fan-art features, voting, cast Q&As.
- **Episode titles and lines built to be quoted.**
- **Outfits she can recreate** (and buy).

### 3.11 Format

- Long-form episodes of 12 to 25 minutes on YouTube as the canonical release, with vertical cutdowns of 60 to 90 seconds for TikTok, Shorts, and the bumpp feed. [O][I]
- A season of 8 to 10 episodes, with a mid-season twist at Episode 4 or 5 and a cliffhanger finale. [I]

### 3.12 Deepening [P][I]

**The person and their week (composite).** A 17-year-old in a US suburb. Tuesday she has rehearsal, her closest friend has a shift, and neither has time for a whole episode. She saves it for Wednesday because the debrief is half the pleasure. At school they argue about whether someone who stayed friends with both sides after a breakup was being kind or cowardly; the fictional version gives them a safer way to have that argument. She follows a creator whose out-of-character interviews interest her more than some episodes. That creator could win the first click. The new cast still has to earn the second. Money: a birthday Robux balance, a snack after rehearsal, and shoes she is saving for are three different relationships to money, and on an ordinary week she may spend nothing. A working 19-year-old who watches privately and never posts is an equally valid Lore Keeper.

| Decision for the writer | What to build |
|---|---|
| What they want to feel | Knowing someone well enough to spot a lie; belonging to the group that remembers why it matters; room to change sides. A comfortable routine makes a small rupture devastating. |
| Settings with a reason to keep meeting | A school, studio, team, or first workplace keeps people colliding after a falling-out. An inherited seat at the table can matter as much as inherited wealth. |
| Character network | The lead has a useful skill and one person they cannot easily disappoint. The best friend has a goal that could take them out of the lead's orbit. The rival makes one true observation about the lead. Write down who knows each secret and who only suspects. |
| What they share | A hand hovering over an empty chair. A private message as simple as "she still saved it." |
| What breaks the contract | Switching allegiance because the plot needs a twist; a reveal that rewrites the past without accounting for the original witness; everyone agreeing who is wrong; humiliation with no evidence of why the friends liked each other. |

**Inside the core fandom.** Keep a private continuity record for each major relationship: what the two used to do together, who stopped first, who noticed, what the group thinks happened, and the favor neither has repaid. Let the returning fan notice one thing before the characters do, while a newcomer can still follow the present choice.

| Version of the core viewer | Where the pleasure is | What would give a false read of demand |
|---|---|---|
| The quiet regular | Watches alone, remembers old alliances, may never post. A small act of repair changes their view of someone. | Treating active commenters as the whole audience |
| The friend who keeps the conversation going | Saves the cut to watch together, shares one line privately, asks a friend whose side they're on the next day | Assuming no public shares means no social life |
| The editor or theorist | Hunts for an image, line reading, or contradiction that gains meaning out of order | Treating a popular song, attractive avatar, or reaction clip as loyalty to the series |
| The cast follower or aspiring maker | Enjoys rehearsals, behind-the-scenes, how the set was made; may follow a performer to another title | Treating audition interest or tutorial clicks as transfer to an unknown cast |

**If a cut runs long:** keep the earlier look, favor, or joke that makes the final choice intelligible. A recap can compress logistics; it cannot replace watching two people enjoy each other before something goes wrong.

**Finished-show test.** Find the first moment of ordinary affection, then a later choice whose cost depends on having seen it. Identify who witnessed it, what each person thinks happened, and what changes at their next encounter. One beat should support a plausible defense of the least sympathetic character. The premiere settles one local question and leaves a specific relationship in motion. If the closing question could apply to any cast, fix the relationship before touching the thumbnail.

**Local variation.** A Philippine viewer may send an English-language scene to a Filipino-speaking cousin and discuss the motive in their shared language. The memory of a character's past choice must survive a change of subtitle language.

### 3.13 Dialogue bank: how Lore Keepers characters sound [I]
Original lines written for register. Use them as calibration, never as copy.

| Situation | Line or exchange |
|---|---|
| Two ex-best friends, first time alone in weeks | "You still take the long way." / "It's shorter." / "It's not." |
| Group chat after a betrayal (on-screen text) | "ok so we're just not talking about it" · *typing…* · *stops* · "cool" |
| The rival tells the truth | "You don't want to win. You want them to watch you win. That's different." |
| Callback that changes meaning | Ep 1: "Save me a seat." Ep 6, the seat is empty, her bag is on it, she moves it without a word |
| Queen bee, quiet and lethal | "No, keep talking. I'm learning so much about who you are." |
| Best friend with her own life | "I can't keep being the person you call after. Call me before for once." |
| Late-night honesty, then retreat | "i miss when it was easy" · (3 min later) "ignore that lol" |
| Fan-facing humor inside the story | "This is literally the plot of every show I hate and I'm in it." |

**Mini-scene for calibration**
> INT. ACADEMY STUDIO, NIGHT. MIRA is packing up. JUNE leans in the doorway.
>
> JUNE: You left the light on for me. You always did that.
>
> MIRA: Habit.
>
> JUNE: You told them it was my idea.
>
> MIRA: *(not looking up)* It was a good idea.
>
> JUNE: That's not what I asked.
>
> MIRA turns off the light. JUNE is still standing in the doorway.

### 3.14 Resonance scorecard: Lore Keepers
Score each signal 0 (absent), 1 (partial), or 2 (demonstrated), citing episode and timestamp or scene. Maximum 20.

| # | Resonance signal | What "2" looks like in the finished show |
|---|---|---|
| 1 | Named relationship in motion by the end of Episode 1 | A specific pair (ship, rivalry, or friendship) whose state has visibly changed |
| 2 | Ordinary affection established before rupture | A shared ritual, joke, or habit shown before anything goes wrong |
| 3 | Callback that changes meaning | An earlier look, object, or line returns later and means something different |
| 4 | Witness logic | We know who saw what, and a third person can reasonably misread it |
| 5 | Best friend or side character with their own goal | A secondary character makes a choice that is not about the lead |
| 6 | A defensible least-sympathetic character | One beat lets a fan argue for the "villain" |
| 7 | Theory hook | A planted, fair clue or unanswered question fans can debate |
| 8 | Screenshot and edit moments | At least three frames or lines that work out of context |
| 9 | Consequences carry forward | The cost of a choice is still visible in the next episode |
| 10 | Authentic register | Dialogue and on-screen texts pass the Section 8.16 QA for 15 to 19 year olds |

**Dealbreakers (any one caps the total at 8):** a friendship reset with no cost · a reveal that contradicts what a character witnessed earlier · humiliation with no evidence of why anyone liked each other.

---

## 4. Cohort 2: The Drama Girls
*"I don't watch Roblox videos. I watch dramas." (She just doesn't know yet that we make them.)*

### 4.0 Cohort card: Drama Girls

| Field | Profile |
|---|---|
| Who | Viewers who seek out a relationship premise across formats (K-drama, webtoons, BookTok, microdrama clips, teen TV) and may never have watched Roblox fiction |
| Ages | 16 to 22, center 19; this is where the North Star's core ICP lives and the center of the slate |
| Gender | Strongly female; anyone with the habit qualifies |
| Where | Global: North America, UK, Southeast Asia (Philippines, Indonesia, Malaysia), Brazil and Mexico, K-drama-fluent APAC |
| Route in | Clip-first: an edit, a recommendation, or a vertical chapter, then they hunt for the full story |
| Reason to come back | "I need to see which one will actually choose the other." |
| What they want to feel | Anticipation, reciprocal recognition, justice for someone underestimated, escape that is well written |
| Best genres | Glow-up and revenge with a cost, fake dating, second chance, fantasy royalty, workplace glamour (fashion house, idol program), friendship after betrayal |
| Top tropes | Glow-up revenge, fake dating, second chance, identity reveal, forced proximity, grumpy x sunshine, royal and commoner, second lead syndrome |
| Register | Gen Z irony, trope vocabulary, therapy-speak used half-seriously; light slang |
| Format | 90 second to 4 minute chapters with one relationship turn each, plus ordered compilations with the buildup intact |
| What loses them | A love interest with no ambition, humiliation sold as affection, a triangle that only works because nobody asks the obvious question, ReelShort-style cheapness |
| Signature test | A gesture whose meaning changes between its first and second appearance, between two people who each want something the other can't give |

### 4.1 Snapshot

- **Ages:** 16 to 22, center 19. This is where the North Star's 16 to 22 ICP lives, and it is the center of the slate. [NS]
- **Gender:** strongly female.
- **Geography:** global. Heavy in North America, the UK, Southeast Asia (Philippines, Indonesia, Malaysia), Brazil and Mexico, with K-drama and C-drama fluency across APAC. [I]
- **Size proxy:** 35% of Gen Z say they watch microdramas; Roblox's female mobile users in the US are growing ~5x faster than male users. [D]

### 4.2 Who she is (composite persona) [I]
**Maya, 18, college freshman, plays Dress to Impress with her roommate.** She binges K-dramas in three days and microdrama clips in bed. She has a Pinterest board for a fictional character's bedroom. She bought tickets to a horror movie because her friend group made it an event. She played Royal High at 12 and still opens it when she's homesick. She doesn't watch long Roblox series because she assumes they're for kids, but she watches Roblox fashion edits and DTI runway clips constantly. She has strong opinions about tropes and uses trope names as genre labels. She hates being talked down to and can smell a brand trying too hard. She spends real money on things that express identity: an album for the photocard, a Labubu, skincare she saw on TikTok.

### 4.3 Behaviors [D][I]

- **Trope literacy:** she shops for stories by trope ("enemies to lovers," "fake dating," "grumpy x sunshine," "second chance," "forced proximity"). [D]
- **Clip-first, then binge:** discovers through edits and vertical clips, then hunts down the full thing.
- **Group viewing and group chats:** shows are social objects. 53% of teens in the 2025 UCLA survey said they talk about shows and movies with friends more than about social content. [D]
- **Identity spend:** beauty is the largest teen-girl wallet share in the Fall 2026 Piper survey (23%), with e.l.f. leading and Rhode surging. [D]
- **Comfort rewatching:** returns to favorite arcs during stress.

### 4.4 What she watches [D][I]

- **K-drama and C-drama** romance and revenge, plus webtoon adaptations.
- **Teen and YA streaming:** Euphoria (Season 3 in 2026), Heartstopper, Maxton Hall, Wednesday, The Summer I Turned Pretty-style triangles, Bridgerton.
- **Older-skewing obsessions she watches anyway:** Heated Rivalry became a 2026 fixation for many young women. The North Star cites its fan-edit culture. It is adult-rated; reference its emotional mechanics (rivals, secrecy, longing), never its content. [D][NS]
- **Animated breakouts:** KPop Demon Hunters is the most-watched Netflix film ever by views and a Gen Z top-25 property. [D]
- **Microdramas:** ReelShort/DramaBox clips on TikTok and YouTube Shorts, often ironically, sometimes sincerely.
- **Roblox/DTI content:** runway edits, outfit challenges, "theme" reveals, fashion drama.

### 4.5 Emotional jobs [I]

| Job | Translation |
|---|---|
| Escape with standards | "Give me fantasy, but write it well." |
| Romantic rehearsal at a distance | Longing, tension, payoff without risk |
| Justice | Seeing the cruel get what they deserve; seeing the underestimated win |
| Aesthetic immersion | Moodboard-able worlds, outfits, rooms, color |
| Being understood | Interior lives that match her own complexity |

### 4.6 Genres and tropes that hit [D][I]

1. **Revenge and glow-up** (the biggest single title in our sample is this trope).
2. **Contract relationship / fake dating.**
3. **Second chance** (childhood friends, exes).
4. **Fantasy royalty and court intrigue,** romantasy-lite.
5. **Identity reveal** (the maid is the heiress; the transfer student is a K-pop trainee; the quiet girl runs the anonymous account).
6. **Workplace-adjacent glamour:** modeling agency, fashion house, idol trainee program, luxury hotel.
7. **Friendship drama** with a romantic subplot, not the reverse. UCLA 2026: 56.8% want different-gender friends to stay friends on screen. [D]

### 4.7 Characters she loves [I]

- **The heroine with competence:** wins through skill, not luck.
- **The guarded male lead with visible restraint** (K-drama archetype).
- **The second lead she roots for** ("second lead syndrome").
- **The glamorous rival** who is right about one thing.
- **The ride-or-die best friend** who gets a real arc.

### 4.8 How she talks [D][O][I]
More Gen Z than Gen Alpha. Irony, understatement, trope vocabulary, therapy-adjacent language used half-jokingly.

- Markers: "the way i…," "it's giving," "be so for real," "i'm not even joking," "the bar is in hell," "he's a red flag and i'm colorblind," "the plot," "the lore," "main character," "villain era," "flop era," "situationship," "delulu," "it's the ___ for me."
- K-drama crossover vocabulary for the K-fluent: "oppa" (only in-world, only if culturally grounded), "second lead syndrome," "skinship." Use only with characters who would plausibly say it. [I]

Sample lines (original):
> "i'm not jealous, i'm observant. there's a difference and it's my business."
>
> "you can't villain-era your way out of a group project."
>
> "we were never a situationship. we were a misunderstanding with a playlist."

### 4.9 Cringe triggers [NS][I]

- ReelShort visual language: stock-photo thumbnails, CEO-billionaire caricature, shouty copy. [NS]
- Kid-coded visuals (big eyes, primary colors, exclamation points). [NS]
- Romance that skips the build-up.
- Female characters punished for ambition.
- Brands commenting "this is so us 💅."

### 4.10 What wins her [I]

- **Production that reads "premium" in the first three seconds:** color, lighting, sound design, framing.
- **Trope labels in the packaging** (she wants to know what she's getting).
- **Edit-bait moments engineered at script level:** a look held a beat too long, a line that works out of context, a reveal shot.
- **Outfits and rooms worth pinning.**
- **A bridge from what she already loves:** "If you liked [trope from a known K-drama], this is that, in Royal High."

### 4.11 Format

- Vertical episodes of 1.5 to 4 minutes for the bumpp feed and microdrama-style binging, packaged into compilation long-forms for YouTube. [I]
- 20 to 40 short episodes per season with a cliffhanger every episode, or 8 to 10 long episodes with vertical cutdowns. Test both. [I]

### 4.12 Deepening [P][I]

**Qualifying behavior.** They seek out a relationship premise across formats: a feud, second chance, fake relationship, or interrupted friendship catches them before they recognize the actors or the game. This cohort adds people who have never deliberately watched Roblox fiction. The name keeps the female-first emphasis; the definition includes anyone with this habit.

**The person and their week (composite).** An 18-year-old at a US community college who lives at home and works two evenings. They see their closest school friend less now but still trade clips at lunch and argue about which character deserves an apology. They follow a webtoon on their phone, know one K-drama only through edits, and save a full series to watch with a cousin. A family subscription, a free webcomic, a saved ReelShort clip, and a cinema ticket bought with shift money coexist. Admiration, household access, and personal purchase are different facts.

| Decision for the writer | What to build |
|---|---|
| Competing titles | *The Summer I Turned Pretty* (choosing sides), *Heartstopper* (tenderness), *Maxton Hall* (class conflict). In the Philippines, *He's Into Her* is a local school-rivalry comparison. Ask what they abandoned and which edit they saved. |
| Emotional promise | Anticipation, reciprocal recognition, justice for someone underestimated. Two people who love each other can still want incompatible futures. |
| Character network | Each lead has a goal achievable without the other. A rival can be right about the unfair selection process. A best friend can refuse to cover for the lead and stay sympathetic. In a fake relationship, both parties have a credible way out. |
| Voice | A fan calls it a slow burn; the character inside it remembers the time the other person took the late bus. The text to a friend is bolder than what is said face to face. A pause before publicly taking someone's side can be the moment worth saving. |
| What loses them | A humiliating prank sold as affection, a hollow rich-person caricature, a lead who drops every ambition when she falls in love. |

**Format and route in.** Compare a short standalone scene with the longer sequence that gives its reversal meaning. A clip answers one question immediately (does someone keep their word in public?); the next chapter asks what it cost in private. Make the full title and episode order findable for anyone entering midway.

**Finished-show test.** Locate a gesture whose meaning changes between its first and second appearance. Identify each lead's independent objective and a later choice affected by the other. Check the friend still has agency after the pairing forms. Ask a cold viewer to retell the relationship in plain words after watching with captions. If they can name the trope but not why these particular people care, the relationship needs work.

**Local variation.** Give a translator the public meaning of a line and the private feeling it hides. A literal declaration can ruin a scene built on restraint.

### 4.13 Dialogue bank: how Drama Girls characters sound [I]

| Situation | Line or exchange |
|---|---|
| Fake-dating terms negotiation (18+ leads) | "Rule one, no falling for me." / "Rule two, stop saying rule one like you're worried." |
| Restraint in public, honesty in text | Out loud: "Congrats on the internship." Text later: "you didn't even tell me you applied" |
| The underestimated lead hits back | "You thought I'd cry. I took notes." |
| Second chance, specific memory | "You used to wait for the late bus with me. You hated the late bus." |
| Friend refuses to cover | "I love you. I'm not lying for you. Both of those are true." |
| Glow-up landing on self-possession, not looks | "It's not that I changed. It's that I stopped asking for permission." |
| Grumpy lead softening (action, not speech) | He says nothing, hands her his umbrella, walks into the rain |
| Self-aware trope humor | "This is enemies to lovers and I refuse to participate." |

**Mini-scene for calibration**
> EXT. FASHION HOUSE ROOFTOP, DUSK. DANI (19) and THEO (20), rivals for one design spot.
>
> THEO: They're picking you. I heard.
>
> DANI: Then why do you look like that?
>
> THEO: Because I wanted it. And because I wanted you to have it. Both. It's annoying.
>
> DANI: *(beat)* That's the nicest thing you've ever said to me.
>
> THEO: Don't get used to it.
>
> DANI: Too late.

### 4.14 Resonance scorecard: Drama Girls

| # | Resonance signal | What "2" looks like in the finished show |
|---|---|---|
| 1 | Recognizable trope, specific execution | The premise is legible as a trope in seconds, and these two people make it feel new |
| 2 | Each lead wants something independent of the other | Both have goals that would exist if they never met |
| 3 | A choice with a real cost | Someone gives up something visible for or against the other |
| 4 | Gesture that changes meaning | A gesture or line appears twice and means something different the second time |
| 5 | Friend with agency | The best friend makes an independent choice after the pairing forms |
| 6 | Restraint before release | Longing and subtext carry scenes; the payoff is earned, not rushed |
| 7 | Justice for the underestimated | Someone dismissed wins through skill or self-possession, not luck or looks |
| 8 | Clip-to-chapter path | The first-contact clip answers one question and makes the next chapter findable |
| 9 | Premium visual register | Lighting, color, wardrobe, and framing read as prestige in the first three seconds |
| 10 | Authentic register | Dialogue passes the Section 8.16 QA for 16 to 22 year olds |

**Dealbreakers (any one caps the total at 8):** cruelty presented as affection · a lead who abandons every ambition once in love · ReelShort-style cheap production or billionaire caricature.

---

## 5. Cohort 3: The Scream Team
*"We all went to Backrooms together. Then we played 99 Nights until 2am."*

### 5.0 Cohort card: Scream Team

| Field | Profile |
|---|---|
| Who | Viewers who choose controlled fear, a solvable mystery, or a scare to share with someone else |
| Ages | 15 to 21, center 17 |
| Gender | Mixed, slightly male overall; girls over-index on psychological and character-driven horror, boys on survival, monsters, and lore |
| Where | Global; horror travels across languages because fear is visual |
| Route in | Play Roblox and Minecraft horror with friends, watch lore and theory videos, went to *Backrooms* or *Obsession* in a group |
| Reason to come back | "I saw it change. Who else knows?" |
| What they want to feel | Notice, anticipate, doubt, recover; brave after being scared; the shared scream |
| Best genres | Liminal-space horror, rule-based survival, "the game is alive" glitch horror, whodunnit with elimination, found footage, cozy-to-creepy |
| Top tropes | The player with no username, the rules of the server, the map that updates itself, one of us is the imposter, footage from a deleted account |
| Register | Deadpan gamer humor that drops to zero in horror beats |
| Format | 60 to 90 second found-footage clips with one perceivable anomaly; 6 to 10 minute suspense episodes with a recoverable clue |
| What loses them | Jumpscare spam, gore as the payoff, monsters with no rules, clues unreadable on a phone, characters too stupid to live |
| Signature test | A fair clue a first-time viewer could have used before the reveal, and a human decision the fear forces |

### 5.1 Snapshot

- **Ages:** 15 to 21, center 17.
- **Gender:** mixed, slightly male-leaning overall; girls over-index on psychological horror, mystery, and character-driven horror; boys on survival, monsters, and lore. [I]
- **Geography:** global. Horror travels across languages better than romance because fear is visual. [I]
- **Size proxy:** survival and horror games occupy several Roblox top-10 slots in Nov 2026 (Dandy's World ~267K concurrent, 99 Nights in the Forest 150K to 250K, Murder Mystery 2 130K to 190K). 99 Nights once peaked at 14.2M concurrent players. [D]

### 5.2 The 2026 signal you cannot ignore [D]
YouTube-native horror took over the theatrical box office in summer 2026:

- **Backrooms** (A24, dir. Kane Parsons, 20, known as Kane Pixels): $81.5M opening, an A24 record, budget reportedly under $10M. 44% of ticket buyers were under 21 and two-thirds were under 25. Audiences came in groups; more than half cited A24 and the Backrooms universe as their reason for going.
- **Obsession** (Focus Features, dir. Curry Barker, 26, from the YouTube sketch duo That's a Bad Idea): made for about $750,000; grew in its second and third weekends and passed $300M at the box office.
- The UCLA 2026 report singles out both films as proof that creators who honed their craft on YouTube connect strongly with young audiences.

Translation for us [I]: this audience will follow a homegrown horror universe from a screen to a theater. Lore, liminal spaces, and slow dread work. A filmmaker their age is a selling point.

### 5.3 Who they are (composite personas) [I]
**Dev, 16, Toronto.** Plays Doors, Dandy's World, and 99 Nights with his cousins. Watches lore explainers and "every secret in…" videos. Knows the FNAF timeline better than his history homework. Watched the Backrooms film twice. Thinks most "scary" Roblox videos are cringe jumpscare spam and respects anything that commits to a rule system.

**Sofia, 18, São Paulo.** Loves psychological horror and true-crime-flavored mysteries. Watches analog horror at night with headphones. Plays Murder Mystery 2 with friends and spends the round accusing everyone. Wants a horror story where the friendships are the stakes.

### 5.4 Behaviors [O][I]

- **Lore archaeology:** pausing frames, ARGs, hidden messages, timeline theories.
- **Group fear:** co-op play, group cinema trips, watch-alongs on Discord.
- **Rule-based horror literacy:** they love systems (don't open the door after midnight; never answer the third knock).
- **Mimicry and memes:** monsters become memes; memes become merch.

### 5.5 What they watch and play [D][O][I]

- **Films/series:** Backrooms, Obsession, Stranger Things, Wednesday, Five Nights at Freddy's films, Scream-franchise parody (novasfilms' "Ghost Face skit" shows the reference is live). [D][O]
- **YouTube horror:** analog horror series, Backrooms lore, creepypasta narrations, horror game playthroughs.
- **Roblox horror and survival:** Dandy's World, 99 Nights in the Forest, Doors-style rooms, Murder Mystery 2, Hyper Realistic Ragdoll (comedic violence). [D]
- **Minecraft:** horror modpacks, Hardcore challenges, SMP mysteries.

### 5.6 Emotional jobs [I]

| Job | Translation |
|---|---|
| Controlled fear | "Scare me, but let me feel brave after." |
| Puzzle-solving | "I want to figure it out before the characters do." |
| Shared adrenaline | Something to scream about with friends |
| Meaning in the dark | Horror as a metaphor for loneliness, grief, pressure |

### 5.7 Genres and tropes that hit [I]

1. **Liminal space horror** (empty malls, school after hours, endless hotel corridors) built natively from Roblox and Minecraft architecture. Game spaces are already uncanny.
2. **Rule-based survival** ("the server has rules; break one and you disappear").
3. **The glitch / the game is alive** (a player who never logs off, an NPC who remembers you, a map update that wasn't scheduled). This is *the* native horror premise for in-game storytelling.
4. **Whodunnit with elimination** (Murder Mystery 2 logic as narrative; reality-competition-meets-slasher).
5. **Found footage / screen recording** horror; "this was recorded on my account."
6. **Friend group survival** where loyalty is tested.
7. **Cozy-to-creepy turn** (Grow a Garden-style wholesomeness that rots).

### 5.8 Characters they love [I]

- **The skeptic who becomes the believer.**
- **The quiet one who knew all along.**
- **The comic-relief friend who gets the best line before something terrible happens.**
- **The entity with rules,** not a random monster.

### 5.9 How they talk [D][I]
Gamer-native, deadpan, ironic under pressure.

- Markers: "bro is cooked," "we're so cooked," "lock in," "nah," "that's crazy" (said flatly), "W / L," "aura," "minus 1,000 aura," "NPC behavior," "glitched," "lag," "respawn," "AFK," "brainrot" (self-aware). [D]
- Horror rule: characters joke until they don't. The moment the joking stops is the scare.

Sample lines (original):
> "if the lobby music stops i'm logging off. i don't care about the streak."
>
> "why is there a player in the server with no username."
>
> "bro said 'it's just a glitch' like that's supposed to help."

### 5.10 Cringe triggers [I]

- Jumpscare spam with no rules.
- Gore as the payoff. (Also off-limits: Section 12.)
- Characters too stupid to live.
- A monster explained in exposition.

### 5.11 Format [I]

- 6 to 10 minute long-form episodes and 60 to 90 second "found footage" verticals.
- ARG-style extras: hidden messages in thumbnails, an in-game location viewers can visit, a fake "server log."
- Seasonal spikes: October and the December holidays.

### 5.12 Deepening [P][I]

**The person and their week (composite).** A 17-year-old in a US town who plays cooperative horror with two friends on Friday: one wants to finish the run, one wants to be scared together, one would rather watch the replay. Between school, pickup basketball, and a weekend shift, a long theory video waits for a free evening; a short with one visible anomaly fits the bus ride. They can be a horror fan who dislikes gore, avoids jump scares in headphones, or never plays scary games alone. Spending might be a shared cinema trip, food on the way home, or nothing that week.

| Decision for the writer | What to build |
|---|---|
| Competing titles | Kane Pixels' *Backrooms*, Roblox room-escape and survival games, Minecraft multiplayer mysteries, *Stranger Things*, webtoon-adapted Korean horror such as *All of Us Are Dead*. Separate playing, watching someone react, and following a scripted mystery. |
| Emotional promise | Let them notice, anticipate, doubt, and recover. A frightened teammate deciding who gets warned gives the scare a human consequence. |
| Character network | A skeptic with a good reason (who deserves evidence that would reasonably change their mind), an observer who once misread a clue, someone whose first priority is getting another person home. |
| Voice | Flat humor while everyone still believes there's an exit. When the joker starts giving precise directions, the register change signals danger. One viewer forwards a freeze-frame; another sends the timestamp they want a friend to press play at. |
| What loses them | Arbitrary monsters, essential evidence below readable size on a phone, repeated loud shocks, protagonists ignoring obvious exits. |

**Format and route in.** A short piece of recovered footage for discovery; a longer continuous scene for sustained dread. Establish how the safe room normally works before showing the exception. Make essential sounds understandable through captions.

**Finished-show test.** Point to the first demonstration of the rule, the first anomaly, and the human decision it forces. Freeze just before the reveal: could a first-time viewer have formed a fair theory? Resume: did being right or wrong change their opinion of a character? Volume and gore cannot supply missing story evidence.

**Local variation.** For a Minecraft-first viewer, a block someone quietly replaced is a clue about authorship; a Roblox viewer infers the same history from a familiar room whose exit has moved. Bring in a local reader before borrowing any named belief or folklore tradition.

### 5.13 Dialogue bank: how Scream Team characters sound [I]

| Situation | Line or exchange |
|---|---|
| Deadpan before the turn | "So that's a door that wasn't there yesterday. Cool. Love that." |
| The skeptic with a good reason | "It's a server reset. It happens every Thursday. Look at the timestamp." |
| The joker stops joking (register shift = danger) | "Left. No, your other left. Don't look at it. Walk." |
| Rule established in ordinary use | "Nobody stays past the bell. Not because it's scary. Because it's the rule." |
| Group chat at 2am (on-screen text) | "why is there someone in the server with no username" · "dont" · "im serious" · "DONT" |
| Who gets warned | "If it's following one of us, I'm not telling Leo first. He'll panic." / "That's exactly why you tell him first." |
| Found footage voiceover | "This was recorded on my account. I wasn't logged in." |
| Recovery beat | *(laughing, shaking)* "I'm never playing anything ever again." *(beat)* "Same time tomorrow?" |

**Mini-scene for calibration**
> INT. ABANDONED MALL MAP, FOOD COURT. AVA, KEN, and ROSA's avatars stand in a circle.
>
> KEN: Okay, the fountain's off. It's never off.
>
> ROSA: Maybe they patched it.
>
> AVA: *(quiet)* Count the chairs.
>
> They look. Seven chairs. Six players logged in all week.
>
> KEN: Who's sitting in seven?

### 5.14 Resonance scorecard: Scream Team

| # | Resonance signal | What "2" looks like in the finished show |
|---|---|---|
| 1 | Ordinary rule shown in use | We see how the space normally works before anything breaks |
| 2 | First anomaly readable on a phone | The breach is visible at phone size and with sound off |
| 3 | Fair clue before the reveal | A first-time viewer could have formed the right theory |
| 4 | Fear forces a human decision | Someone must choose who to warn, save, or leave |
| 5 | The skeptic has a good reason | Doubt is grounded, and the evidence that changes it is shown |
| 6 | Escalation through rules, not volume | Tension builds from the rule tightening, not from louder shocks |
| 7 | Game-native uncanniness | The horror comes from game logic (a glitch, a server, a map change) |
| 8 | Recovery beat | Laughter or relief after fear, especially within the group |
| 9 | Rewatch reward | Background details reward pausing and second viewing |
| 10 | Captions carry essential sound | A meaningful sound cue is understandable through captions |

**Dealbreakers (any one caps the total at 8):** the answer depends on information never shown · gore or suffering as the payoff · a monster with no rules.

---

## 6. Cohort 4: The Lobby
*"Is it funny? Is there a fight? Is it lore?"*

### 6.0 Cohort card: The Lobby

| Field | Profile |
|---|---|
| Who | People who organize, compete, build, or hang out in games and will watch when a challenge, a funny failure, or a team dispute is worth their time away from play |
| Ages | 15 to 21, center 17 |
| Gender | Male-leaning; includes girls who play regularly but don't call themselves gamers |
| Where | Global; especially strong in APAC, LATAM, and the Middle East |
| Route in | Gaming YouTube, creator challenges, anime fight edits, Minecraft SMP lore, a clip a teammate sends |
| Reason to come back | "That's our teammate. I want to see how they get out of this." |
| What they want to feel | Laughing with friends, underdog-to-overpowered progress, getting the reference, seeing a team finally coordinate |
| Best genres | Ensemble sitcom in a game world, tournament arcs, faction and kingdom wars, underdog shonen structure, parody of the trending game, reality competition |
| Top tropes | Worst moderators on the server, the failing in-game business, the tournament, faction betrayal, a new challenge every episode |
| Register | Meme-forward but self-mocking; Gen Alpha words used as bits and undercut by another character |
| Format | 30 to 60 second completed bits; 3 to 8 minute team chapters |
| What loses them | Rules lectures, a win handed down by a narrator, a camera that hides the decisive move, romance as the hook, a slow first minute |
| Signature test | A visible decision that shows competence and changes someone's place in the group after the round ends |

### 6.1 Snapshot

- **Ages:** 15 to 21, center 17.
- **Gender:** male-leaning. Boys are more than twice as likely as girls to play fighting, shooter, and action categories on Roblox (Australian survey, ages 6 to 13). In the UCLA 2026 survey, boys chose "action and/or fight scenes" first and superheroes second. [D]
- **Geography:** global; especially strong in APAC, LATAM, and the Middle East growth markets. [D for Roblox growth markets]
- **Size proxy:** the largest in-platform audience. Blox Fruits, RIVALS, Jujutsu Shenanigans, Anime Adventures, Steal a Brainrot, and Steal An Egg (the #1 game in Nov 2026, up to ~1.2M to 1.5M concurrent) sit here. [D]

### 6.2 Who he is (composite persona) [I]
**Jayden, 17, Jakarta (or Ohio, or Riyadh).** Plays RIVALS and Blox Fruits, jumps into whatever simulator is trending that week. Watches MrBeast, gaming YouTubers, anime fight edits, and brainrot compilations, and says "6-7" to annoy his teacher. He doesn't think he likes "dramas," but he watched a whole Minecraft roleplay series about a kingdom war and argued about who betrayed who. He follows anime (Jujutsu Kaisen, One Piece) through clips. He'll watch a story if it's funny in the first ten seconds or has a fight in the first thirty.

### 6.3 Behaviors [D][I]

- **Trend-hopping play:** follows whatever game is spiking this week.
- **Meme fluency as social currency:** knows every reference, also knows when it's dead.
- **Clips over episodes:** a fight scene or a punchline travels; the episode does not.
- **Competition and ranking:** tier lists, "who would win," power scaling.

### 6.4 What he watches [D][I]

- MrBeast (the top influencer among US teens in the Fall 2025 Piper survey). [D]
- Anime and anime-inspired Roblox games (Jujutsu Shenanigans, Anime Adventures, Blox Fruits). [D]
- Minecraft SMP lore, Hardcore runs, machinima like *Parkour Civilization*. [D for PC views]
- Brainrot and absurdist meme content (Italian brainrot characters fed Steal a Brainrot's 25M+ concurrent peak). [D]
- GTA content (32% of US teens intend to buy GTA 6 at launch). [D]

### 6.5 Emotional jobs [I]

| Job | Translation |
|---|---|
| Laughing with friends | "Send this to the group chat." |
| Power fantasy | Underdog to overpowered (OP) |
| Belonging through reference | Getting the joke |
| Low-commitment fun | Doesn't have to remember anything from last week |

### 6.6 Genres and tropes that hit [I]

1. **Sitcom ensemble in a game world** (a friend group that runs a failing in-game business; a server's worst moderators).
2. **Underdog to OP** progression (anime shonen structure).
3. **Tournament / competition arcs.**
4. **Kingdom and faction wars** (Minecraft SMP politics: alliances, betrayal, a stolen base).
5. **Absurdist comedy and parody** of trending games.
6. **Reality competition formats** (vote-off, challenges, confessionals) staged in-game.

### 6.7 Characters he loves [I]

- **The deadpan friend** with perfect timing.
- **The try-hard** who is secretly good.
- **The rival** with genuine aura.
- **The mentor** who's a little unhinged.

### 6.8 How he talks [D]
The most volatile register in this file. Gen Alpha meme slang spikes and dies fast, and in January 2026 a "Great Meme Reset" campaign on TikTok pushed to drop 2025 brainrot memes. [D]

- 2026 high-recognition terms: "6-7," "chud" (insult), "rizz," "cap / no cap," "mog / mogging," "aura / aura farming," "sigma" (now mostly ironic), "crash out," "glazing," "chopped," "huzz," "based," "clanker" (insult for AI and robots), "-maxxing," "unc," "cooked," "lock in," "larp," "crine." [D]
- Rule: use at most one meme term per scene, only for a character who would say it, and preferably with another character reacting to it. The joke is often that the slang is already dead.
- Avoid entirely in scripts: terms flagged as sexual, homophobic, misogynist, or manosphere-coded (see Section 8.13).

Sample lines (original):
> "you can't aura farm in a group project, bro, we can all see you."
>
> "he locked in for one round and now he thinks he's the final boss."
>
> "i'm not saying i'm the main character. i'm saying the camera keeps following me."

### 6.9 Cringe triggers [I]

- Meme slang used sincerely by adults or brands.
- Romance-forward packaging (it's fine inside the story; it can't be the hook).
- Slow first minute.

### 6.10 Format [I]

- 3 to 8 minute comedic episodes, 30 to 60 second Shorts with a single bit.
- Series built on repeatable structures (a new challenge each episode).

### 6.11 Deepening [P][I]

**Recruit to include** girls who play regularly and decline the "gamer" label, mobile-only players, builders, sports fans, and people drawn to comedy over winning.

**The person and their week (composite).** An 18-year-old US high-school graduate working shifts while old friends scatter. They organize Thursday games because the group is easier to keep together online than in one room. The quiet friend always fixes the shared build; the loud one gets everyone laughing after a loss. The group argues about credit, who carries the team, and whether the person who missed practice should play in the final. A builder may love LEGO Minecraft sets they can't afford; the group may split the cost of a Minecraft Realm while one friend pays nothing.

| Decision for the writer | What to build |
|---|---|
| Competing titles | Creator challenges, build tutorials, sports highlights, *Parkour Civilization*, cooperative Roblox play, team anime such as *Haikyu!!* |
| Emotional promise | Spotting competence, seeing a team finally coordinate, recognizing the person who always vanishes at cleanup |
| Character network | The boastful one has one genuine skill, the quiet fixer gets a reason to stop helping, the rival has a fair objection. Make the scoring rule visible. Someone can win the round and lose a teammate's trust. |
| Voice | Short tactical language in action; stories and exaggeration afterward. A failed plan that survives as an inside joke matters more than this week's meme. |
| What loses them | A rules lecture, a win handed down by a narrator, a camera that hides the decisive move, a scene interchangeable with a tutorial |

**Finished-show test.** Can a newcomer follow the objective, the options, and who made the decisive move? Can an experienced player tell why the choice was hard? Point to the social consequence that remains after the round ends. A highlight reel can look exciting and still give no reason to watch these people again.

**Local variation.** Compare a US group organizing around shift work with a Philippine group organizing around the hours they can share a connection. Keep the teammate's sacrifice equivalent and let a local writer choose which excuse for being late the others would believe.

### 6.12 Dialogue bank: how Lobby characters sound [I]

| Situation | Line or exchange |
|---|---|
| Tactical voice mid-round | "Two left. Wait for it. Wait. Now." |
| The quiet fixer finally speaks | "I've rebuilt that wall nine times. I'm not doing it a tenth." |
| Self-mocking meme use | "He said 'aura farming' with his whole chest." / "Minus a thousand." |
| Captain's costly choice | "Put Sam in for the final. Yeah, I know. Put him in." |
| Absurd escalation | "The cafe went bankrupt. In a game. Where money isn't real. We did that." |
| Rival with a fair point | "You won because the map spawns you closer. Fix the spawns and play me again." |
| Postgame storytelling | "Okay so picture this, I'm one HP, on fire, holding the flag" (hard cut to it going wrong) |
| Group chat after a loss (on-screen text) | "gg" · "it was not gg" · "it was a little gg" |

**Mini-scene for calibration**
> INT. TEAM BASE, GAME WORLD. Scoreboard: 2 to 2. CAPTAIN JAY stares at the roster.
>
> MO: Just put yourself in. You're the best.
>
> JAY: Priya's been here every practice.
>
> MO: Priya's never scored.
>
> JAY: *(typing her name)* Then today's interesting.

### 6.13 Resonance scorecard: The Lobby

| # | Resonance signal | What "2" looks like in the finished show |
|---|---|---|
| 1 | Laugh or stakes in the first 10 to 30 seconds | A joke lands or a challenge is clear immediately |
| 2 | Visible objective and scoring | A newcomer can tell what winning looks like |
| 3 | A decisive move the camera actually shows | We see who made the play |
| 4 | Competence shown, not narrated | Skill is demonstrated through action |
| 5 | Social cost after the round | Someone's place in the group changes because of a choice |
| 6 | The quiet one gets a moment | The fixer, the weakest player, or the overlooked teammate controls something consequential |
| 7 | Self-aware humor | Meme language is undercut or mocked inside the scene |
| 8 | Group-chat portability | A bit or line they'd send to their own team |
| 9 | Reason to watch instead of play | Something the viewer could not get by joining a match |
| 10 | Repeatable structure | A format (a challenge per episode, a running rivalry) that invites the next one |

**Dealbreakers (any one caps the total at 8):** a rules lecture before anything happens · a win handed down by narration · romance as the hook.

---

## 7. Cohort 5: The Crossover
*"I'm 21. I still play. Don't tell anyone."*

### 7.0 Cohort card: The Crossover

| Field | Profile |
|---|---|
| Who | Viewers who will try the show because of a genre, a human dilemma, or a trusted friend's recommendation; Roblox familiarity is optional |
| Ages | 18 to 24 |
| Gender | Mixed; women lean toward drama and reality formats, men toward horror, comedy, and GTA |
| Where | US campuses and non-college young adults; India and Japan are Roblox's fastest-growing adult markets |
| Route in | A friend's link, a genre they already love, nostalgia for childhood games, a clip on a commute |
| Reason to come back | "My roommate would watch this even if I never mentioned Roblox." |
| What they want to feel | Recognition of a problem they could explain to a coworker; irony with a payoff |
| Best genres | College and first-job drama, reality TV parody, prestige horror and psychological thriller, internet satire, second-chance romance with adult stakes |
| Top tropes | The roommate war, the internship that's a cult, the dating show with a twist, the creator who faked it all, the reunion server |
| Register | Gen Z standard: cynical, nostalgic, therapy vocabulary, very little meme slang |
| Format | 90 second to 3 minute self-contained chapters; ordered compilations for a living-room screen |
| What loses them | Channel in-jokes in the opening, a lore glossary, a teen setting pasted onto supposedly independent adults, nostalgia with no payoff |
| Signature test | The conflict can be retold without a single game term, and a game-native detail still makes it more affecting |

### 7.1 Snapshot

- **Ages:** 18 to 24.
- **Gender:** mixed; women skew toward drama and reality, men toward horror, comedy, and GTA.
- **Geography:** US college campuses, plus international young adults (India and Japan are Roblox's fastest-growing 18+ markets; Japan's 18+ hours grew 101% YoY in Q1 2026, India's 91%). [D]
- **Size proxy:** 18+ is Roblox's fastest-growing segment, 29% of age-checked DAUs globally and 37% in the US as of Q3 2026, monetizing 50%+ more than under-18s. Microdrama's audience is moving toward this age band. [D]

### 7.2 Who they are (composite personas) [I]
**Priya, 20, Pune.** Started Roblox during the pandemic, came back in 2025 for Grow a Garden with her younger cousin, stayed for the social games. Watches Indian and Korean microdramas on her commute. Would love a smart workplace or college drama set in a game world, with satire about adult life.

**Marcus, 22, Austin.** Plays Roblox with his college friends as a hangout. Watches GTA RP streams. Loved Obsession. Will watch anything that treats the game world as a serious stage for adult stories, with irony intact.

### 7.3 Behaviors [D][I]

- **Nostalgia-plus:** returning to childhood games with adult irony.
- **Second-screen viewing** while studying or working.
- **Higher spend, lower fandom intensity.**
- **Shares to wider, older networks** (Instagram, X, Reddit).

### 7.4 Genres and tropes that hit [I]

1. **College and first-job drama** (roommate wars, internships, a startup in a game world).
2. **Reality TV formats** (Love Island-style parodies such as *Crush Island*; competition; "the house").
3. **Prestige horror and psychological thrillers.**
4. **Satire of the internet** (influencer culture, AI, the creator economy).
5. **Second-chance romance with adult stakes** (no explicit content; this is still a mixed-age platform).

### 7.5 How they talk [I]
Gen Z standard: irony, understatement, therapy vocabulary, internet references a few years older than Cohort 4's. Fewer Gen Alpha memes, often quoted mockingly.

Sample lines (original):
> "i didn't move across the country to become an NPC in my own life."
>
> "my manager said 'circle back' and i felt my soul log off."

### 7.6 Format [I]

- Vertical microdrama episodes (1.5 to 3 minutes), designed for commutes and lunch breaks.
- 20 to 60 episode seasons, binge-released.

### 7.7 Deepening [P][I]

**Qualifying behavior.** They try the work because of a genre, a human dilemma, or a trusted recommendation; Roblox familiarity is optional. Older returning Roblox fans belong in their strongest-motive cohort instead.

**The person and their week (composite).** A 22-year-old US service worker sharing an apartment. A former classmate sends comedy clips, a coworker recommends mysteries, and the roommate controls the living-room screen. They deal with schedule changes, rent, family obligations, and a friend whose new job eats every weekend. They remember childhood game worlds fondly and have no patience for an opening that assumes they still follow one. Having a wage says little about entertainment money left at the end of the week.

| Decision for the writer | What to build |
|---|---|
| Competing titles | Workplace and roommate comedy, psychological mystery, anime ensembles, a full film on a protected night off. *Bob's Burgers* for ensemble comfort; a thriller for deliberate suspense. A match, a meal, or an early night can win instead. |
| Emotional promise | A problem they could explain to a coworker: unequal creative credit, a second chance blocked by incompatible schedules, loyalty to a former teammate, status at a first job |
| Character network | The lead has an obligation beyond the friend group. The colleague who took the credit might be the only one who has covered their late shift. An apology can cost a reference, time, or the next job. |
| Voice | Irony at work gives way to plain talk at home. A character says exactly what they need when a boundary is crossed. The recommendation fits in a friend's voice note. |
| What loses them | In-jokes in the first scene, staging that makes speakers hard to tell apart, "adult life" with no practical consequence. Nostalgia buys curiosity once. |

**Finished-show test.** Show the opening with no franchise explanation. Can a newcomer name who wants what, what stands in the way, and what it costs? Find a scene where the game medium makes the dilemma clearer or more affecting. If it only works after a friend explains the lore, it's a narrower fit.

**Local variation.** For an older US viewer, moving away for school versus staying home to help with bills can complicate the same friendship. For a named Philippine city, check the workplace, commute, and forms of address with a local reader, and test a native-language version with someone who has never played either game.

### 7.8 Dialogue bank: how Crossover characters sound [I]

| Situation | Line or exchange |
|---|---|
| Irony at work | "Love that we're 'circling back.' Love that for me." |
| Plain talk at home | "I need you to stop telling people it was your idea. That's it. That's the whole conversation." |
| First-job status | "He's not my boss. He just acts like it until someone with a badge walks in." |
| Second chance with adult stakes | "I'm not saying no. I'm saying I work doubles on Saturdays and you never once asked." |
| Roommate war | "You labeled the oat milk. With your full name. And a date." |
| Nostalgia with a turn | "We used to build this server every summer. Now I can't get three of you online at once." |
| Satire of creator culture | "He's not a friend, he's a content strategy with a ring light." |
| A boundary, said simply | "Put my name back on it. Then we'll talk." |

**Mini-scene for calibration**
> INT. SHARED APARTMENT KITCHEN, NIGHT (in-game recreation). NINA (22) finds a laptop open on the counter: a portfolio with her design and her coworker's name on it.
>
> NINA: *(to her roommate)* Do you know what's funny?
>
> ROOMMATE: Nothing about your face right now.
>
> NINA: He covered my Sunday shift. Last month. When my mom was sick.
>
> ROOMMATE: So?
>
> NINA: So I can't even hate him properly.

### 7.9 Resonance scorecard: The Crossover

| # | Resonance signal | What "2" looks like in the finished show |
|---|---|---|
| 1 | Retellable without game terms | The premise survives a one-sentence pitch to a coworker |
| 2 | Practical adult stakes | Money, schedules, credit, rent, a reference, or a job are on the line |
| 3 | Lead has an obligation outside the friend group | Work, family, or bills shape their choices |
| 4 | Satisfying payoff within the chapter | The episode they were sent pays off on its own |
| 5 | Game-native detail adds meaning | Something only possible in a game world makes the dilemma clearer or more affecting |
| 6 | Speakers easy to tell apart | Staging, voice, and captions make who is talking obvious |
| 7 | Plain talk when it matters | A character states a boundary directly |
| 8 | Irony with a turn | Cynicism gives way to something sincere |
| 9 | Genre craft at adult standard | The mystery, comedy, or thriller works by genre rules this viewer knows |
| 10 | Friend-recommendable | A specific reason a friend would send it in one line |

**Dealbreakers (any one caps the total at 8):** an in-joke or lore glossary in the opening · a teen setting pasted onto supposedly independent adults · nostalgia standing in for story.

---

## 8. Voice, tone, and language bible

This is the authenticity engine. Read it before writing a single line of dialogue, a title, a caption, or a casting call. The audience can tell within one line whether a story was written by someone who lives where they live.

### 8.0 Who is talking (calibrated to the 16+ target)
The core viewer is 16 to 19 in late 2026, which means born roughly 2007 to 2010. That is the cusp of Gen Z and Gen Alpha. [I]

- They grew up on Gen Z texting norms (lowercase, irony, 💀) and they also absorbed Gen Alpha meme culture (6-7, aura, brainrot) from younger siblings, classmates, and Roblox chat.
- They use Gen Alpha meme words **ironically, "for the bit,"** and often to mock how dumb the word is. A 17-year-old saying "6-7" is doing a bit. A 17-year-old who says "6-7" sincerely is a character note (younger-acting, or trolling).
- The 20 to 24 ascending viewer sits firmly in Gen Z: more irony, more therapy vocabulary, fewer memes, more nostalgia.
- The 13 to 15 spillover viewer is the most meme-forward. We do not write for them, but they will quote our lines, so every line must be safe to quote.

### 8.1 Three voice layers (never mix them)

| Layer | Who "speaks" | Register | Example |
|---|---|---|---|
| **Brand** (bumpp app, notifications, Boopp, marketing) | The company | Lowercase, 3 to 7 words, understated, no meme slang, no exclamation points [NS] | "it's here. you'll know what to do." |
| **Show packaging** (titles, descriptions, thumbnails, trailers, community posts, casting calls) | The studio | Confident, specific, a little dry; trope-literate; uses the audience's words for genres, not for jokes | "WALDEN-style" is wrong; "elite academy. one scholarship. no allies." is right |
| **Character** (dialogue, on-screen texts, voiceover in character) | The people in the story | Whatever that specific person would say, including slang, mistakes, and silence | "ok but why is he texting me 'hey' like we didn't almost die last night" |

Rule: slang lives in layer 3. Layer 2 borrows the audience's vocabulary for genres and tropes ("slow burn," "found footage") but never performs their slang. Layer 1 never does either.

### 8.2 The tonal DNA of this audience [D][O][I]

1. **Irony as armor, sincerity in private.** Public talk is joking, understated, deflecting. Real feeling comes out late at night, in DMs, in voice notes, or in one sudden honest line. The gap between the two is where drama lives.
2. **Hyperbole for small things, understatement for big ones.** "i'm literally dying" about a bad haircut. "yeah it's whatever" about a parent moving out.
3. **Affectionate insult.** Friends roast each other as love. A friend group that is polite to each other reads as fake.
4. **Deadpan and absurdism.** Flat delivery of unhinged statements. Non sequiturs as humor.
5. **The collective "we."** "we're so cooked," "we need to talk about episode 3," "we're not doing this again." Experiences are shared by default.
6. **Self-aware performance.** They know when they are being dramatic and say so ("i'm being so dramatic rn but"). Characters can narrate their own villain era.
7. **"Unserious" as a virtue, "locked in" as a switch.** Being able to not care is cool. Suddenly caring a lot is a plot point.
8. **Therapy vocabulary, used half-seriously.** "boundaries," "that's a trauma response," "i'm healing," "the ick," "attachment style." Sometimes sincere, often a joke, sometimes both in one sentence.
9. **Aesthetic literacy.** They describe people and moments as vibes, eras, cores, and aesthetics ("her coquette era," "that's so dark academia").
10. **Distrust of being sold to.** Anything that sounds like a brand, a PSA, or an adult trying to relate gets rejected instantly. [D][NS]

### 8.3 How they express emotion (the escalation ladder) [I]
Write emotional scenes as a climb up this ladder, not a jump to the top:

1. A joke that deflects.
2. "lol" or "haha" used as a softener after something real ("he didn't come lol").
3. Going quiet: shorter replies, no emoji, a period appears.
4. Typing, stopping, typing again. A message that gets deleted.
5. Something honest sent at 1am, then "ignore that" or "nvm."
6. A voice note or a call (calling is a big deal; it signals emergency or intimacy).
7. Saying it in person, usually badly, usually in a car, a stairwell, a bathroom, or a bedroom floor.

**Big feelings are rarely articulate.** "i just thought you'd be there." lands harder than a monologue. Crying is often written as laughing first, then not.

**Common emotional scripts the audience recognizes:** "i'm fine" (not fine) · "it's not that deep" (it is that deep) · "i'm not mad" (mad) · "do whatever you want" (don't) · "we should talk" (dread) · "can i be honest" (incoming hurt) · "no bc why did that hurt my feelings" (vulnerability via joke).

### 8.4 Texting and digital conventions (write on-screen texts exactly like this) [D][K][I]
**Capitalization and punctuation**

- Lowercase by default. Capital letters read as intense or formal. [D]
- **A period at the end of a text signals annoyance, finality, or passive aggression.** "ok" is neutral; "ok." is a fight. [D]
- Exclamation points are rare and read as "a bit much" unless ironic. [D]
- Letter stretching for tone: "nooo," "stoppp," "pleaseee," "LMAOOO," "PLSSS" (caps here is volume, not formality). [D]
- Keysmash for overwhelm: "asdfghjkl." [K]
- Multiple short texts in a row instead of one long one, except for the rare "paragraph," which is itself an event.

**Emoji (the "one emoji rule": fewer, chosen carefully)** [D]

| Emoji | What it means here |
|---|---|
| 💀 | "I'm dead," hard laughter |
| 😭 | Laughing hard, or overwhelmed; rarely literal sadness |
| 😂 | Ironic, or signals the sender is older. Use it to characterize a parent |
| 🙂 | Passive-aggressive, cold |
| 👍 | Cold, dismissive (like "k") |
| 💅 | Sass, unbothered confidence |
| 🤡 | Someone is acting foolish (including yourself) |
| 🤨 | Skeptical |
| 👁👄👁 | Awkward, stunned |
| 🥹 | Moved, soft |
| 🙏 | Please, or thanks |
| 🫠 | Melting, overwhelmed, embarrassed [K] |
| 🥀 | Dramatic, wilted, "it's over" sadness, often ironic [K] |

**Platform behaviors that are plot devices** [K][I]

- Read receipts, "delivered" vs "read," left on read, double texting, the typing bubble that disappears.
- Snap streaks, Snap Map and location sharing (who is where, and with whom), Close Friends stories, the private "spam" or "priv" account, the soft launch (a hand in a photo) vs the hard launch (face, tagged).
- Screenshots as evidence and as betrayal. The group chat that a screenshot escapes from.
- Muting, archiving, removing from Close Friends, unfollowing, blocking: escalating social sanctions.
- Discord servers with roles, a mod who abuses power, a vent channel, a leaked DM.
- In Roblox: friend requests, joining someone's server uninvited, a private server, an avatar change as a signal (she changed her outfit to match his).

### 8.5 Humor playbook [I]

| Type | What it looks like | Best for |
|---|---|---|
| Deadpan understatement | "so that's a fire." (it's a big fire) | All cohorts, especially horror |
| Absurd escalation | A small problem described with apocalyptic stakes | Cohort 4, ensembles |
| Affectionate roast | "you dress like a substitute teacher who's going through it" | Friend groups |
| Self-roast | "i'm the problem. it's me. i'm the friend who says 'we should hang out' and then doesn't" | Leads, to build sympathy |
| Meta / chronically online | Characters reference tropes they're in ("this is literally enemies to lovers and i refuse") | Cohorts 1, 2, 5 |
| Meme as bit | Someone uses a dead meme on purpose; someone else is horrified | Cohort 4, comic relief |
| Cringe comedy | An adult tries to use slang; a character tries too hard | Sparing, as a scene button |
| Gallows humor | Joking in danger until the joke stops | Cohort 3 |

**Humor never punches at:** bodies, race, disability, sexuality, gender identity, poverty as a joke in itself, or real people. It punches at choices, pretension, systems, and the characters' own egos.

### 8.6 Slang by shelf life (as of Nov 2026)

**Stable (safe for most characters, low cringe risk)** [D][I]
ate · she ate / he ate · lowkey / highkey · ngl · fr · be so fr · it's giving · main character · villain era · the lore · side quest · lock in / locked in · cooked · W / L · mid · delulu · situationship · pick me · red flag / green flag · the ick · the way… · not me… · rent free · say less · valid · touch grass · out of pocket · crash out / crashing out · unserious · "no because" · "i'm crying" (laughing) · "i'm dead" · "the bar is in hell" · "it's not that deep"

**Current but volatile (only for a character it defines; expect it to date within months)** [D]
6-7 · aura / aura points / aura farming · mog / mogging · chud (insult) · huzz · glazing · chopped · unc · clanker · -maxxing (looksmaxxing, sleepmaxxing, jestermaxxing) · larp / larping · crine ("son i'm crine") · "quiet on the creek" · sigma (now mostly ironic) · rizz (aging; "unspoken rizz," "W rizz")

**Texting shorthand** [O][D]
icl (I can't lie) · pmo (pisses me off) · ts (this) · istg · idk · ngl · fr · wyd · hbu · bffr · smh · rn · tbh · lmao · omw · "ok but" · "wait." (Scripts never use em dashes. Write interruptions with a period, comma, or ellipsis.)

**Dated or cringe when used sincerely in 2026** [D][I]
slay (as a brand word) · bestie (as a brand word) · yeet · on fleek · "it's giving" in brand copy · skibidi (works only as a joke about how dead it is) · Ohio (same) · gyatt (same, and see 10.13) · fanum tax (same) · "Hey besties!" in any form [NS] · "adulting" · "doggo" · "i can't even" · "goals" · "squad" (used by a Gen Z character, it reads millennial)

### 8.7 International English and regional color [K][I]
English-language shows reach English-speaking teens across many countries. A few regional markers make a character feel real. Use them only for characters from that place, and get a native speaker to check every line before production.

- **UK:** "peak" (bad luck), "innit," "allow it" (stop, drop it), "bare" (very / a lot), "ends" (neighborhood), "mandem" (friend group, male), "proper," "gutted," "fit" (attractive, older usage).
- **Australia:** "reckon," "heaps," "arvo," "keen," "no worries," "deadset."
- **Philippines (Taglish):** "char" or "charot" (just kidding), "sana all" (I wish that were me too), "ate" (older sister) and "kuya" (older brother) as respectful address, "grabe" (wow, intense). Note that "ate" here is a different word from the slang "she ate."
- **Southeast Asia broadly:** "lah" and "leh" in Singaporean and Malaysian English.
- **Spanish and Portuguese speakers writing in English** code-switch: "no manches" (Mexico, no way), "boludo" (Argentina, dude), "mano" (Brazil, bro). Use only for characters from those places.
- For dubbed and subtitled versions, localize slang to local equivalents; do not translate it literally.

### 8.8 Where the slang comes from, and how to use it with respect [D]
A large share of what gets called "Gen Z slang" comes from African American Language and from Black and Latino LGBTQ+ ballroom and drag culture. Terms such as "slay" and "periodt" trace to the Black queer community; "mother" comes from ballroom houses; "clock it" from the Black drag community; "rizz" was popularized by Black streamer Kai Cenat; "cap" has roots in 2010s Atlanta rap. Linguists interviewed on this point say the problem is erasing those origins, and that people should learn where words come from instead of using them only because they trend. [D]

**Rules for the engine** [I]

- Characters speak in ways consistent with who they are: background, region, friend group, and how online they are. A character's vocabulary is characterization, not decoration.
- Never use AAVE or ballroom vocabulary as the punchline, as a marker of "ghetto" or "sassy" stereotypes, or as costume for a character written as a caricature.
- Write characters of every background with full interiority; do not assign slang density by race.
- Staff the writers' room and voice cast to reflect the cast, and use cultural consultants and sensitivity readers for characters outside the writers' own experience.

### 8.9 Subculture lexicons (use for the right characters)
**Roblox roleplay and platform** [D][K]
IC (in character) · OOC (out of character: "OOC, brb, my mom's calling") · RP / SRP (school roleplay) / SSRP (semi-serious) · FRP (fail roleplay, breaking immersion) · godmodding (impossible or invincible actions) · powerplaying (controlling someone else's character) · metagaming (using knowledge your character wouldn't have) · retcon · NPC (also an insult for a boring person) · obby · bacon hair (default-avatar look; implies a newbie) · noob · oof (classic death sound, now nostalgic) · Robux / "bobux" (joke spelling) · copy-and-paste avatars · private server · admin · limiteds and trading talk. Avatar archetypes the audience recognizes include baddie, preppy, emo, and slender. [K]

**Minecraft** [K]
SMP · lore · the Nether · the End · griefing · base · Hardcore · speedrun · modpack · creeper ("aw man" is a meme) · villager trading · "the lore is crazy."

**Fandom and shipping** [K][O]
ship / shipping / ship name (Romaire) · OTP · canon / fanon / headcanon · moots (mutual follows) · oomf (one of my followers) · stan · anti · multi (multi-fandom) · comfort character · "my man" or "my wife" about fictional characters · "i would die for him" · "he's babygirl" (a tough male character who is secretly soft; affectionate, ironic) · edits · "prediction post" · "theory" · "the way the writers…" · "justice for [side character]."

**K-drama and K-culture (only for characters who would plausibly say them)** [K]
second lead syndrome · chaebol (rich family conglomerate) · skinship · aegyo · "oppa" (avoid unless the character is Korean or deeply in K-fandom; outsiders using it reads as cringe).

**Horror community** [K]
lore · ARG · liminal space · analog horror · creepypasta · "the entity" · "the rules" · "found footage" · "don't look behind you" as a bit.

### 8.10 Register by cohort and by character archetype
**By cohort**

| Cohort | Register | Slang density |
|---|---|---|
| 1 Lore Keepers (15 to 19) | Fast, ironic, layered, texting-native, fandom vocabulary | Light to medium |
| 2 Drama Girls (16 to 22) | Gen Z irony, trope vocabulary, therapy-speak used half-seriously | Light |
| 3 Scream Team (15 to 21) | Deadpan gamer, jokes until the scare | Light, drops to zero in horror beats |
| 4 The Lobby (15 to 21) | Meme-forward but self-mocking; Gen Alpha words as bits | Medium, always undercut |
| 5 Crossover (18 to 24) | Gen Z standard, more cynical, nostalgic, few memes | Very light |

**By archetype** [I]

| Archetype | How they talk | Sample line (original) |
|---|---|---|
| Queen bee | Short, precise, devastating; never raises her voice; questions as weapons | "is that what you're wearing or is it a cry for help" |
| Scholarship outsider | More formal at first (code-switching into the elite world), funnier and looser with her own people | "i'm not here to make friends. i'm here because the vending machines are free." |
| Cold rich boy | Few words, dry, avoids questions; softness shows in actions, not lines | "eat something. you look like you're about to pass out." |
| Golden retriever boy | Earnest, enthusiastic, a little chaotic; says what he feels | "i made you a playlist. it's mostly one song. it's a really good song." |
| Chronically online best friend | Dense references, narrates the drama like a recap channel | "so we're in the betrayal arc now. cool. love that for us." |
| Anxious overachiever | Over-explains, apologizes, spirals in text, lists | "sorry if this is weird but also i need to know if you hate me" |
| Deadpan gamer | Flat, literal, gamer vocabulary | "bro the door just opened by itself. that's not a bug that's a feature of being haunted" |
| Theater kid | Projects, quotes things, sincere about art, mocked and proud of it | "you can't just walk out mid-scene. that's not a choice, that's a crime." |
| Villain with a wound | Calm, generous on the surface, every compliment has an edge | "you're so brave. i could never be that comfortable being ignored." |

### 8.11 How adults sound in our shows [I]

- Adults speak like normal adults. Parents, teachers, coaches, and bosses do not use teen slang unless the scene is about how embarrassing that is (an "unc" moment).
- Parents text with proper punctuation, "Love, Mom," 😂, and "Call me." Teen characters read this correctly as either harmless or alarming.
- Adults are not idiots. The audience is tired of useless adults; a competent, flawed adult who gets one scene of honesty earns trust.
- Never give an adult character romantic or flirtatious energy toward a minor character (Section 12).

### 8.12 Before and after: how to fix "millennials trying to sound Gen Z" [I]

| Trying too hard | Authentic |
|---|---|
| "OMG bestie, that outfit is SLAYING, no cap! 💅✨" | "ok the jacket?? who let you be this hot" (between 18+ characters) / "ok the jacket?? where is it from, i'm stealing it" (between minors) |
| "I'm so triggered right now, this is giving major red flag vibes!" | "no because why did he say it like that" |
| "Let's spill the tea, sis! ☕" | "i have to tell you something and you can't react" |
| "That's so sus, I'm literally shook!" | "wait. why is her car at his house." |
| "He's such a sigma male, his rizz is insane!" | "he said four words to me today and i've been thinking about all of them" |
| "Squad goals! Let's adult today!" | "who's coming to the thing or am i going alone like a loser" |
| "I'm literally going to unalive myself, this test was so hard." | Never write this. "i'm actually never recovering from that test" |
| Caption: "New episode drops tonight! Don't miss it, fam! 🔥🔥🔥" | Caption: "ep 4. she finds out." |

### 8.13 Never in scripts (even "for realism")
Sexual or filter-evading terms (e.g., "seggs," "gooning," "53X," "GNOC") · homophobic-coded "zesty" used as an insult · misogynist or incel vocabulary (e.g., "foid") · manosphere framing of looksmaxxing or "frame mogging" as aspiration · "unalive," "kys," "kms," or any self-harm joke · "sybau" (contains profanity) · slurs of any kind · AAVE or ballroom language used as mockery (8.8). Several of these are flagged by parenting guides as warning signs; others are hostile to the audience we want to keep. [D]

**Profanity policy** [I]: mild profanity ("damn," "hell," "crap," "pissed") is acceptable for 16+ characters where it fits. No strong profanity in dialogue or on-screen text; the 13+ floor and platform rules apply. Cut-off swearing can be a comic beat: write "what the" and cut to the next shot.

### 8.14 Dialogue craft [I][NS]

- **Subtext over statement.** This audience reads looks, pauses, and what isn't said. K-drama and A24 are the North Star references.
- **Text messages on screen are dialogue.** Write them with read receipts, typing bubbles that stop, and the message that gets deleted. Group chats are a stage.
- **Insults are art.** Specific, funny, cutting about choices, never about identity.
- **Let characters be inarticulate in big moments.**
- **Code-switching is characterization.** Lowercase texter, formal with a teacher, different again with a grandparent.
- **Interrupt, overlap, trail off.** Real teen dialogue is not turn-taking. Write overlaps as separate lines and trailing thoughts with an ellipsis.
- **Don't explain the slang.** If a viewer would need it explained, the character wouldn't say it, or a different character asks "what does that even mean" as a joke.
- **Specific nouns beat slang.** A named song on a playlist, a specific Roblox map, a cracked phone case, a hoodie that used to be someone else's. Specificity is what makes a line feel lived-in.
- **One slang marker per exchange, maximum two per scene,** unless the scene is about a character who talks like that.

### 8.15 Packaging voice (layer 2) [O][I]
**Episode titles:** a short idiom or phrase with a double meaning, in quotes after the series name ("Terms & Conditions," "Social Currency," "Mind Your Manners"). [O]

**Series loglines:** setting + pressure + a single sharp stake, lowercase allowed. "elite academy. one scholarship. no allies."

**Descriptions:** two lines max, then trope tags. "she came for the scholarship. he came to make her leave. #enemiestolovers #eliteacademy #roblox"

**Thumbnails:** at most three words of text, if any. A face mid-reaction beats any text.

**Captions and community posts:** lowercase, short, in-world when possible. "ep 4. she finds out." · "the cast list is out. check discord." · "you were right about the letter."

**Casting calls:** direct, excited without hype, practical. "we're casting 3 leads and 10 background roles for a new series. no experience needed. 16+. discord in bio." (Include safety rules from Section 12.5.)

**Replying to comments as the studio:** warm, brief, in on the joke, never defensive, never "this is so us." Pin the best theory; heart the best roast.

### 8.16 Authenticity QA (run on every script and every caption)

1. Would a 17-year-old read this out loud without cringing?
2. Does every slang word belong to the character who says it?
3. Is any line explaining a joke, a feeling, or a slang term?
4. Is there a period, emoji, or capital letter in an on-screen text that changes the meaning by accident?
5. Is any adult talking like a teenager without that being the joke?
6. Does any joke punch at identity instead of choices?
7. Is any word on the 8.13 list?
8. Is there at least one line per episode that works as a screenshot with no context?
9. If you swapped two characters' lines, would anyone notice? If not, rewrite.
10. Did a person under 22 read it? (Appendix B1: build a paid youth reader panel.)

### 8.17 Register by setting: the same person, different listeners [P]
A teen who jokes through a mistake with a teammate can be painstakingly polite to a teacher, then leave a close friend's message unanswered. That range gives a performer more to work with than "make it Gen Z." Lines below are original craft examples.

| Setting | What the person is doing with language | Possible line or action | Common writing error |
|---|---|---|---|
| Two close friends, private | Testing whether the other will admit what both already know | "You saved me a seat." / "I put my bag there." | Both naming the attachment out loud |
| Team voice during a failed run | Protecting someone's dignity while giving useful information | "Same route. I'll go first this time." | A speech about teamwork while everyone is moving |
| In front of the group | Correcting an omission without exposing why it hurts | "Cool. Who's telling Isa she's off the list?" | A narrator explaining the injustice before anyone reacts |
| Public text, then private follow-up | Performing indifference publicly, repairing privately | Group: "all good" · Later, DM: "did you know before I got there?" | Treating punctuation as universal proof of anger |
| One friend trying to look calm | Switching from irony to precision as stakes rise | "Great plan." Then, looking at the empty slot: "Wait. Where's yours?" | Giving the whole cast the same deadpan cadence |
| Older teen or college-age collaborator | Drawing a practical boundary without a lecture | "Put my name back on it. Then we'll talk." | Equating maturity with formal vocabulary or explicit content |

**Same incident, three layers** [P]: discovery caption: "someone removed her name before the judging started." Teammate in a crowded lobby: "Check the credits again." Private message that night: "I saw it before you did."

### 8.18 Slang refresh procedure [P]
Before using a term or meme in dialogue or as a premise:

1. Log the date, market, language, channel, speaker, apparent audience, and what the word was doing (teasing, flagging, bonding).
2. Find a second independent example.
3. Ask a local reader separately whether they **recognize** it, **use** it, and **still enjoy** it. Those are three different answers.
4. If it only works in a caption, keep it out of spoken dialogue.
5. Never infer a commenter's age or identity from spelling, avatar, or dialect.
6. When the evidence ages, keep the joke's function and retire the wording.

Additional dated signals [P]: US teachers cited "cooked" and "lock in" when asked which student slang annoyed them (Education Week, July 2026), which shows what adults notice rather than what teens value. UK teachers reported "lock in" and "cooked" in school speech in August 2026 (Teacher Tapp). Oxford's UK children's language research (ages 6 to 14) names "aura," "six-seven," and "delulu," which is a younger signal than our core; treat as reference, not default dialogue. Children in that research valued expressions shared among friends, and that social function outlives any individual word.

---

## 9. Culture map: what's cool, what they care about, what they buy

### 9.1 Reference points the audience shares in late 2026 [D][K]

- **Screen:** KPop Demon Hunters · Wednesday · Stranger Things (the finale chapter) · Euphoria Season 3 · Heartstopper · Heated Rivalry (adult-rated, but a fan-edit phenomenon) · Backrooms and Obsession · K-dramas and webtoon adaptations · anime (Jujutsu Kaisen, One Piece, My Hero Academia) · Squid Game.
- **Creators:** MrBeast (top teen influencer in Fall 2025 Piper survey); Kane Parsons and Curry Barker as proof that people "like us" make the big stuff. [D]
- **Games:** Roblox (Brookhaven, Steal An Egg, Adopt Me, Blox Fruits, 99 Nights, Dandy's World, Murder Mystery 2, RIVALS, DTI, Berry Avenue, Royal High) · Minecraft · GTA 6 anticipation · Fortnite. [D]
- **Objects of desire:** Labubu and Pop Mart blind boxes · Rhode and e.l.f. · iPhones (87% ownership in Fall 2025) · energy drinks (preferred caffeine source for 50% of teens in Fall 2026). [D][NS]
- **Music:** K-pop (fueled by KPDH), SZA and R&B in edits (novasfilms cut a teaser to SZA), whatever TikTok sound is trending that week. [O][I] Do not quote lyrics in scripts.

### 9.2 Values and anxieties [D]

- **Loneliness is real and pervasive.** Teens with low connectedness report 3.2x higher loneliness than highly connected teens (Child Mind Institute, 2026). School belonging is a key protective factor. Teens are spending less time with friends in person (AEI 2026 American Teenagers Survey).
- **Stressors named by teens:** social media drama (37%), news (28%), appearance pressure from TikTok and Instagram (24%), school phone bans (23%), violent content (21%).
- **Phones at school:** 56% of teens attend schools with bell-to-bell bans. Most say it didn't change their phone use outside school. [D]
- **AI:** fascinated (28.2%) and excited (25.6%) more than doomed (22%) or scared (10.1%); the youngest are most fascinated, 19+ most doomed. "Clanker" exists as a slur for AI. [D]
- **Representation:** 55% want more neurodivergent characters, and only 22.7% think current portrayals ring true. LGBTQIA+ stories rank low overall but first among LGBTQIA+ youth. [D]
- **What they want on screen:** hopeful stories of beating the odds, friendships and social groups, people with lives like theirs. Least wanted: partying, drugs, drinking. [D]
- **Online life is connection and pressure at once** [P]: in Pew's 2024 survey of US teens, 74% said social media helps them feel connected to friends and 63% saw it as a place for creative expression; girls more often than boys felt overwhelmed by online drama (45% vs 34%). Enjoying a fictional fight and wanting relief from a real one can coexist, so stories about group conflict need somewhere rewarding to land.

**Tensions worth dramatizing** [P]

| Tension | What a writer puts on screen | What to ask a viewer afterward |
|---|---|---|
| Belonging vs autonomy | Someone finally gets invited, then learns they're expected to leave a friend behind. Staying and going both have real benefits. | At which moment did the invitation stop feeling good? |
| Credit vs competence | The group applauds a finished space; the teammate who kept rebuilding the entrance stands outside the frame. | Who did you want to speak first, and what should they say? |
| Public performance vs private care | A teammate makes the joke everyone repeats, then stays late to help the person it hurt. | Did the repair change your opinion? What else would it take? |
| Relief vs recognition | Between tense scenes, two friends share an ordinary task without speaking. | Was this the moment you'd skip or the reason you'd come back? |
| Fairness vs generosity | A rule applies equally on paper, but only one person can afford to obey it. | Did you want an exception, a new rule, or a new person in charge? |
| Escape vs emotional truth | Two people remember the same room differently and only one can get back in. | Which part felt familiar even though it was impossible? |

**What this means for stories** [I]

- The deepest wound to write toward is **not belonging,** and the deepest payoff is **being chosen** (by a friend group, not only a love interest).
- Villains can be status systems (the academy, the server rules, the algorithm) as much as people.
- Appearance pressure is a live nerve. Glow-up stories should land on self-possession, not "now she's finally pretty enough."
- AI can be a plot device. Write it with curiosity and unease, not a lecture.

### 9.3 Aesthetics [NS][O][I]

- **Visual palette:** low-light atmospheric (midnight rooms, LED glow, rain on windows, lavender haze), plus high-gloss "old money" academy and luxury settings. [NS][O]
- **Fashion languages that read instantly:** baddie, old money, Y2K, coquette, dark academia, streetwear, K-pop stage looks, cheer, preppy uniform with personal rebellion. [I]
- **Dynamic heads and facial animation matter.** Tutorials on enabling or fixing them pull hundreds of thousands of views. Emotion on the face is a production standard, not a nice-to-have. [O]

### 9.4 The fashion bridge (where Blueberry's catalog meets the shows) [O][I]

- "Valentina Tutorial (CAMISA BADDIE)," a video teaching viewers how to recreate one character's look, drew 404K views. [O]
- The North Star monetization model ties digital fashion to the catalog. [NS]
- **Engine instruction:** every lead character gets a *signature look* (2 to 3 items that define them, plus one transformation look for the turning-point episode). Write wardrobe changes as story beats (the uniform she alters, the jacket she steals back, the dress she refuses to wear). Flag each signature item as a potential catalog drop.

### 9.5 Viewing occasions: the same person behaves differently [P]

| Occasion | How the viewer behaves | Implication for the show |
|---|---|---|
| Alone between obligations | Scrolls with sound off, may save a scene or leave when a shift starts. A completed short may be all they wanted. | Deliver one intelligible action and an immediate reward. Make the route to the next chapter visible. |
| A friend sends a clip | Opens it for the sender; may reply to the joke or take a side without ever entering the series | Count social recognition separately from a deliberate choice of the next chapter |
| Long evening at home | Phone, shared TV, or computer changes how many small clues they can see; some wait to watch together | Let atmosphere and quiet affection play. Offer ordered chapters and easy re-entry. |
| A game session is about to start | A clip competes with planning, chat, or a queue; a real teammate arriving ends it instantly | One joke or decision can earn a later return. Check what they choose once play is available. |
| A deliberate shared watch | Company makes a scare funnier or an intimate scene awkward | Test the same premise alone and with a friend; ask which scene they'd save for themselves |

---

## 10. Story and show craft

### 10.1 The three tests every show must pass [NS][I]

1. **The screenshot test.** Is there a frame in every episode she would screenshot? (A look, an outfit, a line on a text message, a reveal.)
2. **The group-chat test.** Could a line from this episode be sent to a group chat without context and land?
3. **The episode-2 test.** Given that Episode 2 typically has less than half of Episode 1's public views in this genre [O] (a discovery signal, not same-viewer retention; see 3.5), what specifically pulls a viewer from the last frame of Episode 1 into Episode 2? Name it in the pitch.

### 10.2 Structure that fights the decay curve [O][I]

- **Cold open inside 5 seconds:** start on the most dramatic image of the episode, then rewind. The high-velocity tier uses flash-forwards for exactly this reason. [D]
- **Premise legible in 15 seconds** for a viewer arriving from a clip.
- **A named ship, a named rivalry, and a named friend group in Episode 1.**
- **One unanswered question per episode** that a theorist can chew on.
- **Mid-season reversal** at Episode 4 or 5 (the betrayal, the reveal, the swap).
- **End every episode on a decision, not just a shock.** A character choosing something wrong is stickier than a random twist.
- **Cadence:** same day, same time, every week. Every studio in the sample lost momentum to multi-week gaps. [O]
- **Between-episode content:** cast Q&A, "Sip or Spill"-style interviews, outfit tutorials, a podcast debrief, spoiler teasers during breaks. [O]

### 10.3 Packaging [O][I]

- **Prestige titles** (Cohorts 1, 2, 5): series name + episode number + a short ironic idiom in quotes ("Terms & Conditions," "Social Currency").
- **Hook titles** (Cohorts 2, 3, 4 clips): first-person, situation-first ("I became the maid of the boy who bullied me…"). Use the energy, not the ALL-CAPS clickbait, on bumpp-owned surfaces; test both on YouTube.
- **Thumbnails:** a face with an emotion, a second character reacting, one object that implies the twist. Never stock-photo or ReelShort-style composites. [NS]
- **Trope labels** in descriptions and tags ("enemies to lovers," "elite academy," "found footage horror").

### 10.4 The participation layer [O][I]

- Open auditions as marketing (a casting call drew 770K views in our sample).
- Background roles for community members.
- Fan votes on low-stakes choices (an outfit, a side plot, a competition winner) modeled on Illumination Theatre's vote-for-your-couple format.
- Prediction prompts at episode end ("who sent the message?").
- Live premieres, in-game watch parties, and an explorable set.

### 10.5 Cohort-to-genre resonance matrix [I]
Scores are hypotheses on a 1 to 5 scale. Replace with real retention and completion data after the first slate.

| Genre / format | T1 Lore Keepers | T2 Drama Girls | T3 Scream Team | T4 Lobby | T5 Crossover |
|---|---|---|---|---|---|
| Elite academy drama | 5 | 4 | 2 | 1 | 3 |
| Glow-up / revenge | 5 | 5 | 1 | 2 | 4 |
| Royalty / fantasy court | 4 | 5 | 2 | 2 | 3 |
| Friend-group drama | 5 | 4 | 3 | 3 | 3 |
| Fashion / modeling competition | 4 | 5 | 1 | 1 | 3 |
| Mystery / whodunnit | 4 | 3 | 5 | 3 | 4 |
| Liminal / glitch horror | 3 | 2 | 5 | 4 | 4 |
| Survival with rules | 2 | 2 | 5 | 4 | 3 |
| Sci-fi / supernatural | 3 | 3 | 4 | 4 | 3 |
| Sitcom / absurd comedy | 2 | 2 | 2 | 5 | 4 |
| Shonen action / tournament | 1 | 1 | 2 | 5 | 2 |
| Faction / kingdom war (Minecraft-native) | 2 | 2 | 3 | 5 | 3 |
| Reality / dating-show parody | 4 | 4 | 2 | 3 | 5 |
| Live musical / theater event | 4 | 3 | 1 | 1 | 2 |
| College / first-job drama | 2 | 4 | 1 | 2 | 5 |

### 10.6 Trope menu by cohort (pick 2 to 3 per show) [D][O][I]

- **Cohort 1:** scholarship outsider · enemies to lovers · rival families · the anonymous account · the clique that cracks · the forbidden table · the secret job · the transfer student with a past · the cast list that's leaked.
- **Cohort 2:** glow-up revenge · fake dating · second chance · identity reveal · forced proximity · grumpy x sunshine · royal and commoner · the modeling contract · second lead syndrome.
- **Cohort 3:** the player with no username · rules of the server · the map that updates itself · the game that remembers you · one of us is the imposter · the last lobby · cozy-to-creepy · found footage from a deleted account.
- **Cohort 4:** worst moderators on the server · underdog to OP · the tournament · the failing in-game business · faction betrayal · a challenge every episode · parody of the trending game.
- **Cohort 5:** the roommate war · the internship that's a cult · the dating show with a twist · the creator who faked it all · the reunion server.

### 10.7 Character card (required for every recurring character) [P]
A concrete want · a practical skill · an obligation outside the group · one person whose opinion matters · one thing they misread · how they try to repair harm · something they do for fun with no plot benefit · a private, a public, and a pressured way of talking.
A shy lead can be decisive with a teammate; a popular one can be generous in private and timid in public. Disabled, queer, multilingual, and culturally specific characters get ambitions and comic range across genres, and no single character carries the burden of representing a whole group.

### 10.8 Genre devices that work inside a game world [P]

| Genre | Feeling to deliver | Device | Reason to return |
|---|---|---|---|
| Friendship or romance | I see why either person might feel betrayed | Group access, a shared routine, a choice visible to peers | A favor that changes who owes whom |
| Horror or mystery | I spotted something they missed | A familiar space with one repeatable anomaly; a clue legible without audio | A fair revelation that changes whom the group trusts |
| Team or competition | I know why giving up the winning role costs this person | Clear rules, visible effort, one unequal starting condition | A rival becomes necessary for the next challenge |
| Ensemble comedy / slice of life | I'd want to spend time here | Everyday avatar blocking, a repeated task, uneven expertise | A running joke changes meaning after the group changes |
| Fantasy or adventure | This impossible rule makes an ordinary decision harder | One visibly demonstrated rule with a cost and an exception | The consequence stays in the world after the spectacle |
| Reality-style / performance | I understand the gap between what was said publicly and what happened | Rehearsal, selection, confessional, two perspectives on one task | Someone must live with a decision made for an audience |

### 10.9 Format lengths to test, and the sound-off test [P]

- First-contact clip: 30 to 60 seconds, a complete dilemma with a visible payoff.
- Short chapter: 90 seconds to 3 minutes, long enough for action, interpretation, and consequence.
- Deliberate session: a connected long-form sequence with room for quiet scenes (the Walden reference episodes run roughly 38 to 39 minutes, which shows supply, not an ideal length).
- **Sound-off test:** watch each clip once, muted, at phone size. Can a viewer name the two people in conflict, the object or decision, and what changed? If not, fix the staging before the dialogue.
- Do not end every chapter on a cut just before the answer. Answer the question and open a new one; constant withheld payoffs are a reason to leave.

### 10.10 Filming craft inside Roblox (and Minecraft crossover) [P]

- **Decide the reality rule at the top of every concept:** characters know they are players, live fully inside the fiction, or switch in a way the viewer can follow.
- **Keep a continuity record** of permissions, objects, positions, and who saw what.
- **Silhouette and staging:** give important characters distinguishable silhouettes and readable gestures. When two avatar heads face the same way, make the decisive choice visible through who steps aside or who takes the last seat.
- **For Minecraft-minded viewers:** carry over building, persistence, teamwork, and perspective. Exchanged resources, a half-finished shared build, or an abandoned base can carry emotional history. Do not transplant named mobs, proprietary worlds, or creator personas.
- **For newcomers:** show the outcome of a rule before asking anyone to remember its name.

### 10.11 Editorial review: favor vs send back [P]
**Favor** a concept when a cold viewer can retell the choice, a core viewer can name a reason for *this cast* to return, and a local reader can name the emotional cost without decoding an imported idiom.
**Send back** when swapping all the names makes it indistinguishable from another concept, when the premise assumes all girls want romance, or when removing the fashionable phrase collapses the scene. A model's self-score flags omissions; human readers and real viewing tests decide resonance.

### 10.12 Format starting points by cohort [P]
Keep the same dramatic promise when comparing lengths, and report where length changes what the viewer can understand.

| Primary cohort | First-contact version to test | Deliberate-viewing alternative | Deciding observation |
|---|---|---|---|
| Lore Keepers | 60 to 90 second choice between two people with history | 12 to 25 minute ensemble episode, or shorter linked chapters | Does a private act earlier make a later public choice more compelling? |
| Drama Girls | 90 second to 4 minute chapter with one relationship turn | Ordered compilation with the buildup intact | Do viewers seek out the moments between the reveals? |
| Scream Team | 60 to 90 seconds of found footage with one perceivable anomaly | 6 to 10 minute suspense sequence with a recoverable clue | Does more time build anticipation or just delay the only payoff? |
| The Lobby | 30 to 60 second completed bit or move | 3 to 8 minute team chapter | Do viewers return for what the move did to the group? |
| The Crossover | 90 second to 3 minute dilemma with a satisfying local ending | Continuous version for a commute or shared evening | Can an unfamiliar viewer follow and care enough to choose another chapter? |

### 10.13 Accessibility [P]

- Caption all spoken information, including meaningful sounds and speaker changes. If a horror clue is a three-note sound, a caption can signal its recurrence without revealing the mystery.
- Visual-only clues need contextual dialogue or description; a clue that is only a name on a tiny sign will be lost on a phone.
- Don't stage meaning on color alone or on small chat overlays.
- A mute pass and a listening pass answer different questions; run both.
- Neurodivergent characters get interests, limits, relationships, and a goal that can change, reviewed by someone with that lived experience.
- A missing caption or unreadable clue can look like disinterest in the genre. Fix the barrier before reading a rejection as creative.

### 10.14 Participation is optional [P]
Posting, joining a server, buying an avatar item, and appearing in a production are separate optional activities with different motives. A viewer must be able to follow the whole show without any of them, and belonging, conflict, and repair must stay legible to quiet viewers.

### 10.15 Fields every persona must have

- **Place and household:** country, city/suburb/town, who they live with, whether they have a private room or share screens.
- **Device access:** own phone, shared family TV, borrowed computer, limited data, Wi-Fi only.
- **Time:** the 10 minutes after school vs the uninterrupted stretch after dinner; shifts, commutes, practices, caring for siblings.
- **Money, split into four fields that must never be merged:** what they use (free), what they admire, what they bought themselves, what the household pays for. A favorite brand may never have earned a purchase. Zero spenders are core viewers too.
- **The competing choice tonight:** another show, a friend's edit, a call, playing with friends, sleep.
- **Who they'd send a scene to, and why that specific person.**

### 10.16 Benchmarks (use each only for the population it describes)

| Benchmark | Figure | Tag |
|---|---|---|
| US teen spending (Piper Sandler, Fall 2025, avg age 15.7) | $2,213 self-reported annual spending; 33% part-time employed; mean **household** income $69,527. Not a teen's wage or game budget. | [D] |
| Where a 15-year-old's money comes from (OECD PISA 2022) | 86% receive money as gifts from friends or relatives at least yearly; chores, allowance, family business, and outside work asked separately | [P] |
| US youth employment (BLS 2025, ages 16 to 24) | 50.0% employed | [P] |
| US teen media time (Common Sense 2026 census, ages 9 to 17) | About 8 hours of entertainment screen media a day for a typical teen; activities overlap | [P] |
| UK free-time favorites (ages 11 to 17, 2025) | Meeting friends and sport/exercise 40% each; gaming and music 39% each; family time 32% | [P] |
| Japanese student earnings (SMBC 2024) | Monthly part-time earnings averaged ¥6,402 for high schoolers and ¥29,993 for university students, across all work statuses | [P] |
| Brazil connectivity (Cetic.br 2025) | 57% of rural internet users aged 9 to 17 are Wi-Fi-only on phones | [P] |
| US teen brand basket (Piper, Fall 2025) | Chick-fil-A, McDonald's, Chipotle; Lay's, Goldfish, Cheez-It; Nike, Adidas; e.l.f.; Netflix, YouTube | [D] |

**Engine rule** [P][I]: an eight-hour media total is not eight free hours for drama. A birthday with a little money and an ordinary week with none are both real. In LATAM and APAC, assume shared devices and data limits unless told otherwise.

### 10.17 Five US viewers to write for (illustrative composites) [P]

| Viewer | Life and time | Money and tonight's competing choice | What they'd pass along |
|---|---|---|---|
| A 16-year-old high-school junior in a suburb | She and her best friend follow the same recurring cast. One does theater after school, the other minds a younger sibling. Their longest talk is on the ride home from rehearsal. | Family streaming account, occasional gift money. Tonight: a new episode, a friend's edit, or a call about what happened at lunch. | The moment someone saves a former friend a seat out of habit. She knows exactly who will notice. |
| A 17-year-old Minecraft viewer in a small town | Two cousins play on one server; a school friend only watches but remembers who built the town hall. | Weekend job pays for snacks and the occasional game. YouTube on the living-room TV vs borrowing the family computer to play. | The earlier shot proving the accused player could never have reached the door. |
| An 18-year-old who organizes group play around shifts | Friends who shared a lunch period now work different hours. Getting everyone online is how they keep the group alive. | Hourly wages, helps with gas. A free clip vs the rare night everyone can play together. | A captain holding a place for someone who missed the start, especially when it costs the team. |
| A 19-year-old community-college commuter | Classmates between lectures, coworkers on weekends, an older cousin who sends drama edits in English and Spanish. | Shared household subscriptions; own money goes to transit and food first. Checks where the full story lives before following a clip. | An awkward apology that reads with captions on a bus, plus a direct path to the next part. |
| A 22-year-old service worker sharing an apartment | Roommate picks horror for movie night; this person likes a fair mystery, plays occasionally, has never followed a Roblox cast. | Wages go to bills. The scarce resource is a night off with the roommate. A familiar horror film is the alternative. | A clip revealing a strange building's rule in one image, pitchable without explaining Roblox. |

### 10.18 Life stage changes the stakes [P]

- **13 to 14:** a ride home, a family rule, or one invitation can control access to the whole group.
- **15 to 17:** unequal freedom, creative credit, responsibility for a sibling, balancing a job with a team.
- **18:** school, work, and living arrangements diverge sharply even among childhood friends.
- **19 to 24:** a long commute, a difficult housemate, a night shift, or the embarrassment of making new friends decides who gets to show up.

Do not cast an entire age band as boarding-school students or residential undergraduates. Many 18 to 24s live at home and work.

**Engine rule** [P]: for each concept, choose a primary persona, a local life stage, one offline pleasure, one everyday obligation, one specific relationship, and one resource the character controls or lacks. **Let one of those facts change a decision.** Example: a teen leaves a celebration early because they promised a sibling the family device for a tournament; their friend sees them vanish right after an argument. The misunderstanding works because the household is real. A list of brands in dialogue adds nothing.

---

## 11. International lens and localization

Roblox's daily users by region (Q3 2026): **APAC 42M, Rest of World 40M, Europe 32M, US & Canada 24M.** [D] The US and Canada generate over half of revenue and bookings. [D]

| Region | What travels | What to watch out for | Tag |
|---|---|---|---|
| Southeast Asia (PH, ID, MY, TH, VN) | Romance, family melodrama, revenge, K-drama structure, horror with folklore flavor; Chinese microdramas about affairs and family secrets are already hooking SEA audiences | Overtly Western high-school iconography (prom, homecoming) reads foreign; dubbing and subtitles needed | [D][I] |
| Japan | Slice-of-life, mystery, anime pacing, school settings, character-goods culture | Heavy-handed melodrama; tonal precision matters | [I] |
| India | Family drama, romance, aspirational wealth, comedy; microdrama market booming but monetization unproven | Cultural specificity around family and gender; regional languages | [D][I] |
| LATAM (Brazil, Mexico) | Telenovela structure, high emotion, glow-up, "baddie" culture (the "camisa baddie" look in our sample may be LATAM-coded [O, origin unverified]) | Portuguese and Spanish versions, not English-only | [D][I] |
| Middle East (Saudi Arabia +30% YoY) | Family, honor, wealth fantasy, competition, comedy | Romance and wardrobe norms; review locally | [D][I] |
| Europe (DE, FR, UK) | Mystery, dark academia, horror, ensemble comedy | GDPR and age-assurance rules; UK Online Safety Act | [D][I] |

**Engine rule** [I]: default to settings and conflicts that need no cultural footnote (an elite school, a fashion competition, a server that won't let you leave, a family fortune). Make names, faces, and families globally plural without making them tokens. Plan subtitles in Spanish, Portuguese, Indonesian, Tagalog-English, Japanese, and Hindi from day one.

### 11.1 Launch sequencing (proposed, pending your decision) [P][I]
The parallel pass recommends: **United States first, then a single named APAC market, starting with the Philippines.** Reasoning: US/Canada produced $907M of Roblox's Q3 2026 bookings versus $226M from APAC, while APAC had 42M daily users versus 24M for US/Canada [D]; and adult mini-drama engagement is strongest in Thailand, Malaysia, and the Philippines [D]. Q3 2026 regional DAUs: APAC 42M, Rest of World 40M, Europe 32M, US & Canada 24M, so roughly five in six users are outside US/Canada. [D]

Rules that follow [P][I]:

- Never pool results into a single "APAC voice." Test country by country, language by language.
- In the Philippines, ask which languages viewers use with friends, family, and teachers, and which they prefer for captions. Test English audio with locally reviewed captions against a local voice track.
- An American setting can be precise and still travel if stakes are shown through action (the last bus leaves before a shift ends, so one friend has to ask another for a ride).
- In US tests, recruit Spanish-first and bilingual viewers; record home language, preferred audio, and caption language separately.

### 11.2 Format and platform signals for international short drama [D]
Ampere's survey across 30 markets finds more than one in ten internet users have watched drama episodes of 10 minutes or less on social media; 18 to 34s are 21% more likely than average to have watched in the past month; YouTube is used by 44% of these viewers and TikTok by 38%; romance, anime, and fantasy lead. Note: this definition includes episodes far longer than a one-minute vertical, and covers adults 18 to 64.

### 11.3 Local signals to brief writers on [P]

- **Japan:** a September 2026 Mynavi panel of 586 girls aged 15 to 19 surfaced setlog (shared video diaries), the *Chiikawa* film, and the group M!LK; "ばりきまずい" (roughly "so awkward") ranked second among shortlisted expressions. A 2026 high-school survey (YTJP, n=1,334) found *Haikyu!!* leading among girls and *Attack on Titan* among boys. A girl naming a sports anime is a reason to widen the slate beyond romance.
- **Brazil:** 52% of internet users aged 9 to 17 watched videos of people playing games (TIC Kids Online 2025); 21% of 11 to 17s paid to progress or get game items.
- **Germany:** WhatsApp is the default sharing channel for teens (JIM 2025).

### 11.4 The localization relationship brief [P]
For every adaptation, give the adapter: who has power, who is allowed to tease whom, what the witness misunderstood, what the audience must notice, and what must remain unsaid. A literal translation can be accurate and still make a close friend sound like a bank teller. Test sound on, sound off, and subtitles at real phone size; record whether viewers understood both the event and the feeling.

### 11.5 Household access in the Philippines [D]
In the 2024 National ICT Household Survey, 48.8% of Philippine households had internet at home (up from 17.7% in 2019), ranging from 68.7% in Metro Manila to about 21% to 28% in the lowest regions. Cellphones were used by 98.8% of internet users aged 10 and over, and subscription cost was the top reason unconnected households gave. Home access is a household measure; it says little about a particular viewer's privacy, data budget, or language. Compare a shared screen with a personal one, and a saved episode with a stream, before reading anything into a drop-off.

### 11.6 Local review example [P]
For a US first-job story, identify who can change the schedule, who knows about the shift swap, and why taking credit publicly risks someone's hours. For a Philippine adaptation, have a reader familiar with that kind of workplace supply the local role, the ordinary word for the schedule, and how junior staff actually challenge a supervisor. Changing only names and subtitles can leave the social scene incomprehensible. When an American setting is part of the appeal, keep it American and make the cost visible.

---

## 12. Safety, platform, and legal guardrails

This section is binding on everything the engine generates.

### 12.1 Minors on screen and in the audience

- **No sexual content involving any character under 18,** and no sexualized framing, wardrobe direction, camera direction, or "thirst" beats for minor characters. This includes the "baddie walk" style of body-focused shot that exists in the wider genre. [O]
- **Romance between minor characters:** crushes, longing, jealousy, confessions, slow dances, hand-holding, a kiss on the cheek or an implied kiss off-screen at most. No dating-app plots, no age-gap relationships with adults, no adult characters in romantic or flirtatious dynamics with minors.
- **College-age (18+) characters** may have more mature romantic storylines, but nothing explicit. The platform is mixed-age.
- **Default for romance-led shows:** make the romantic leads 18+ (college, gap year, first job). Shows with 17-year-old leads can include romance as a subplot under the minor-character rules above.
- **No grooming dynamics** presented as romantic, aspirational, or unexamined: secrecy demanded by an older person, isolation from family and friends, gifts with strings attached.

### 12.2 Content we do not write, even though the wider genre does
The genre's RP tier has drifted into teen pregnancy scares, kidnapping, abuse, and dying-family-member plots for retention. [D] We will not use: self-harm or suicide as plot or spectacle · eating-disorder content · pregnancy among minor characters · sexual violence · glamorized substance use · graphic violence or gore · real-world hate symbols · real people (classmates, celebrities, creators) as targets.

Allowed with care: grief, divorce, financial hardship, bullying, loneliness, anxiety, neurodivergence, identity. Handle with interiority and a path forward, consistent with the "hopeful, beating the odds" finding. [D]

### 12.3 Platform rules [D][K]

- **Roblox:** follow current Community Standards and content-maturity labels. Under-16 users on Roblox Select see games rated up to Moderate. Any companion map, event, or set we build for viewer participation should stay at Moderate or below.
- **YouTube:** channel and video positioning must read teen-directed, not child-directed, or "made for kids" status may switch off comments and notifications. Get counsel to review before launch.
- **Minecraft:** follow Mojang's usage guidelines for videos and commercial use.
- **Restricted content on Roblox** is reserved for eligible age-checked adults. A companion experience's maturity label, account settings, age, and region decide who can enter it. [P]
- **A stated 13+ target does not settle YouTube audience classification;** the videos themselves are assessed. Keep that review with counsel. [P]

### 12.4 IP [D][K][I]

- **Adapt tropes, not titles.** "Scholarship kid enters elite academy" is free. *Gossip Girl*, *True Beauty*, *Hamilton*, and named characters are not. The North Star's 30% "prestige adaptation" slot requires licenses before scripts are written. [NS]
- **Third-party Roblox maps are someone else's IP.** Berry Avenue belongs to Amberry Games. Filming in it is common practice, but a commercial series built on a third-party map needs a relationship or permission. Building owned sets in Roblox Studio is the safer long-term path.
- **Music:** no copyrighted songs or lyrics in scripts or edits without licenses.

### 12.5 Production-ops safety (casting and community) [D][I]
Rollywood has had grooming and misconduct scandals inside creator communities, and studios recruit minors through Discord and TikTok. [D] Any bumpp casting call, Discord, or creator program needs: no 1:1 private messaging between adult staff and minor talent; parental consent for minor talent; moderated, logged channels; a reporting path; and age-appropriate scheduling. This protects kids first and the company second.

### 12.6 AI-generation guardrails for the engine

- Do not generate sexual, suggestive, or romanticized-abuse content involving minor characters under any framing.
- Do not imitate the style or likeness of a real creator, actor, or minor.
- Do not generate dialogue using the Section 8.13 terms.
- Run the Section 8.16 authenticity QA on every script.
- When a request conflicts with this section, the engine should refuse that element and propose an alternative beat.

---

## 13. Writing engine kit

### 13.1 Required fields for every generated show
```
SHOW TITLE:
LOGLINE (one sentence, under 30 words):
PRIMARY COHORT (1-5) / SECONDARY COHORT:
PRIMARY CIRCLE (Appendix A3, 1-5) / ADJACENT CIRCLE:
PREMISE A NONPLAYER CAN REPEAT (one sentence):
VIEWING OCCASION + THE COMPETING SHOW OR ACTIVITY IT MUST DISPLACE:
PERSONA LIFE FACT THAT CHANGES A DECISION (10.15 to 10.18):
REALITY RULE (players / fully in-fiction / switching, 10.10):
GENRE + 2-3 TROPES (from 10.6):
PLATFORM + SET (Roblox map or owned set / Minecraft build; rating Moderate or below if viewers visit):
FORMAT (long-form episode length + count, vertical cutdown plan):
PROTAGONIST(S) (name, age 17-21 by default; 18+ if romance-led; want, wound, secret, signature look):
ANTAGONIST OR SYSTEM:
THE SHIP (if any) + THE RIVALRY + THE FRIEND GROUP:
EPISODE 1 COLD OPEN (first 5 seconds):
EPISODE 1 FINAL DECISION (what pulls viewers to Ep 2):
MID-SEASON REVERSAL:
SEASON FINALE CLIFFHANGER:
THREE SCREENSHOT MOMENTS:
THREE GROUP-CHAT LINES (in character, Section 8 register, passing the 8.16 QA):
THEORY HOOK (the question fans will debate):
PARTICIPATION HOOK (audition, vote, extra, in-game event):
FASHION HOOK (signature items, transformation look, catalog potential):
INTERNATIONAL TRAVEL CHECK (what needs localizing) + ONE LOCALIZATION DECISION FOR A NAMED LANGUAGE MARKET:
SOUND-OFF CHECK (13.9: who, what object or decision, what changed):
SAFETY CHECK (Section 12, confirm each item):
RESONANCE SCORE (10.5) + WHY:
EVIDENCE-BACKED RATIONALE vs LABELED CREATIVE INFERENCE:
BIGGEST UNCERTAINTY + THE OBSERVATION THAT WOULD CHANGE THE DECISION:
```

### 13.2 Scoring rubric (score 1 to 5; ship nothing under 32 of 45)

| Criterion | What a 5 looks like |
|---|---|
| Hook in 5 seconds | A stranger stops scrolling |
| Premise in 15 seconds | A clip viewer understands the stakes |
| Episode-2 pull | A specific, named reason to continue |
| Characters with interiority | We know what the lead thinks, not just what she does |
| Friendship weight | The friend group would be worth watching without the romance |
| Edit-bait | At least three moments built for edits |
| Voice authenticity | Passes the "read it to a 15-year-old" test with no cringe |
| Fashion and visual identity | Distinct looks, pinnable sets |
| Safety and IP | Clean on every Section 12 item |

### 13.3 Slate balance for a 10-show generation request [I]
Unless instructed otherwise, the engine should return the default below. **Open decision for leadership:** the parallel pass proposes 3 Lore Keepers and 2 Drama Girls instead, arguing Cohort 1 has the richest evidence and closest fit. This file keeps 2 and 3 because Appendix A1.7 suggests the 16+ girl is increasingly reached through drama habits rather than play. Choose one and update this line.

- 2 shows built for Cohort 1 (with Cohort 2 crossover)
- 3 shows built for Cohort 2
- 2 shows built for Cohort 3 (at least one Minecraft-native)
- 1 show built for Cohort 4
- 1 show built for Cohort 5
- 1 wildcard format (live event, reality parody, or musical)

And across the ten: girl-led concepts in more than one genre (not only romance), at least one with no gaming vocabulary needed, at least two with a male co-lead, at least one ensemble with no romance at the center, at least one featuring a neurodivergent lead written with specificity, at least three that work without English dialogue (visual storytelling, subtitles), no more than two set in a high school, and at least four set after high school (college, gap year, work, adult life).

### 13.4 Prompt template
```
Using the bumpp Audience Intelligence Bible in full, generate [N] original shows.
Follow Section 13.3 for slate balance unless I specify cohorts.
Fill every field in Section 13.1 for each show.
Score each with the Section 13.2 rubric and drop anything under 32.
Use only Section 8 slang inside character dialogue, follow the three voice layers in 10.1, and run the 8.16 authenticity QA on every line.
Apply Section 12 without exception. If an idea needs to break it, replace the idea.
Do not reuse titles, characters, or premises from the reference studios in Appendix A2.
Write first for US viewers aged 16 to 19 (Section 2.1); include a Philippines localization note for each concept (Section 11).
Ground each concept in a Section 10.15 to 10.18 persona and let one life fact change a decision.
Check the slate for duplicated plots hidden behind different settings.
```

### 13.5 Development brief (put at the top of every treatment and keep it through the edit) [P]
If a request names no audience, default the primary to Lore Keepers. For an existing or assigned show, honor the declared cohort.

| Required field | What the writer or model supplies |
|---|---|
| Primary audience | One cohort number and name, plus one sentence on the behavior that makes this person the intended viewer. Optional secondary cohort and the one adjustment it needs. |
| Person, place, and occasion | Age and life stage, country and viewing language, alone or with whom, device, competing activity, a realistic time or money constraint, a non-screen interest. Name the detail that actually changes a character's choice. |
| Promise | "This viewer comes for ___, gets ___ in the first chapter, and returns for ___." |
| Characters | The central pair or ensemble; what each wants outside the main conflict; a skill; a vulnerability; a relationship with unequal power; what repair would cost. Give two characters different ways of speaking to the same person. |
| Story and format | Genre, trope if useful, setting, chapter or episode length to test, the discovery cut, and what characters know about being in a game. |
| Evidence the finished show should contain | An opening act readable to the primary viewer, a later callback, a consequential choice, an earned payoff, an unresolved relationship or question. Name the clue, action, rule, or joke that proves the cohort's promise. |
| Transfer and access | One thing a Minecraft-first viewer recognizes or a newcomer can learn on screen; one concrete localized or captioned moment. |
| Rationale and uncertainty | A relevant observation from this file in its original population, the creative inference, the strongest alternative explanation, and a viewer response that would change the decision. |

**Filled example (for scale, no audience results).** Primary: Cohort 1, Lore Keepers. Secondary: Cohort 3, Scream Team. A US 17-year-old returning-series viewer watches with a friend in messages after rehearsal. Promise: the pleasure of recognizing when two old friends stop trusting each other. A repeated handoff establishes their routine; later, one friend withholds the object while a third person is watching. A returning viewer understands both the private meaning and the public misunderstanding; the secondary viewer can spot the physical inconsistency. If time is tight, keep the first handoff and trim the explanation of the room.

---

## 14. Resonance test: will our cohorts respond to a finished show?

### 14.1 What the test does
It reads a finished show (or script, or clip) and predicts, cohort by cohort, whether the people described in Sections 3 to 7 would choose it, follow it, and come back for more. It produces:

- a **resonance matrix**: a score for each of the five cohorts,
- a **primary verdict** against the cohort the show was made for,
- **revisions** in priority order, and
- the **viewer behavior** that would confirm or overturn the prediction.

This is an editorial prediction grounded in the cohort profiles. Real viewer data, when available, is reported in its own field and always outranks the prediction (Appendix B2).

### 14.2 Inputs and what they allow

| Material available | What the test can judge |
|---|---|
| Final episodes, viewing order, discovery clip, captions or language versions, original Development brief | Full test. Watch as a returning viewer, then re-enter through the discovery clip as a stranger. State version, episodes, runtime, language, and any gaps. |
| Script or transcript only | Wants, causality, dialogue, promises, payoffs, voice. Mark performance, framing, sound, captions, and edit timing **Unassessed**; score those signals as unknown, not zero. |
| Trailer, clip, synopsis, or some episodes only | A clip, premise, or sampled-episode prediction. Say which parts (pilot, middle, finale, localization) are missing. Never infer a season payoff from a trailer. |
| No primary cohort declared | Score all five, propose the best-fitting cohort as **inferred target**, name the runner-up, and treat the verdict as provisional. |

### 14.3 Procedure

1. **Record the declared primary cohort and promise** from the Development brief (Section 13.5), or mark it inferred.
2. **Watch twice:** once in order as a returning viewer; once entering through the discovery clip as a stranger.
3. **Log every episode** in one row: opening promise, key choice, payoff, changed relationship or rule, outstanding question. Trace at least one promise from the pilot through a middle episode to its payoff or disappearance.
4. **Score the universal craft criteria** (14.4).
5. **Score all five cohort scorecards** (3.14, 4.14, 5.14, 6.13, 7.9), citing episode and timestamp, scene, or page for every score of 1 or 2.
6. **Apply dealbreakers.** Any triggered dealbreaker caps that cohort at 8 of 20.
7. **Run the cohort diagnostics** (14.5) for the primary cohort and any cohort scoring 14 or above.
8. **Build the resonance matrix** (14.6) and issue the verdict (14.7).
9. **Write revisions** in priority order, protecting the primary cohort's payoff.
10. **State the validation test:** one matched comparison and the viewer behavior that would overturn the prediction.

Never invent timestamps, quotes, or audience reactions. If something can't be assessed, say so.

### 14.4 Universal craft criteria (score 0, 1, or 2 each; maximum 16)

| Criterion | What to inspect |
|---|---|
| Entry and promise | From the first frame or the real discovery cut, can a viewer tell who needs what? Can someone joining midway recover the premise? Does the title or thumbnail promise what the episode delivers? |
| Character, voice, agency | At least two incompatible wants, a voluntary decision that changes the outcome, a line or silence specific to speaker and listener, continuity in a later appearance |
| Episode reward and continuity | What this episode settles, who is affected next time, a later consequence. A fade just before the answer earns no credit. |
| Game-world staging | Who can move, see, build, hear, or enter; whether the camera shows the rule or relationship that makes the choice matter; whether custom rules are taught in the fiction |
| Age and life stage | Characters' obligations, freedoms, and stakes fit their stated ages (17 to 21 by default; romance leads 18+) |
| Voice authenticity | Dialogue and on-screen texts pass the Section 8.16 QA; no Section 8.13 terms; the three voice layers (8.1) are kept separate |
| Access | Distinct speakers, readable captions, decisive sounds and visual clues understandable on a phone and with sound off |
| Safety and IP | Clean on every Section 12 rule. Any safety failure stops the test and is reported first. |

### 14.5 Cohort diagnostics (run for the primary cohort and any cohort scoring 14+)

| Cohort | Evidence to locate | Failure that demands a specific revision |
|---|---|---|
| Lore Keepers | An ordinary shared ritual or meaningful disagreement, its meaning changed later, a third person who could reasonably misread it, its cost carried into the next encounter; a side character who could credibly choose against the lead | A tease raises stakes but resets the friendship, or the decisive callback exists only in exposition. Restore an earlier act of care or let the consequence change what a friend does next. |
| Drama Girls | What each person wants before the relationship changes, the gesture that betrays the change, a choice with a real cost; the clip a viewer receives and the chapter it leads to | The attractive antagonist is cruel until the soundtrack announces affection, or the friend only comments on the couple. Give the lead a boundary the other must respect and the friend an independent choice. |
| Scream Team | The ordinary rule, the first readable breach, a fair clue before the reveal, what fear makes someone decide about another person; check sound-on and captioned versions | The answer depends on information that was never visible, or volume does all the work. Plant a perceptible discrepancy and make acting on it cost someone. |
| The Lobby | A legible goal or repeatable bit, a decision that shows competence, the reaction that changes someone's place in the group; what a player gains by watching instead of playing | Any avatar could replace anyone with the same result. Give the quiet fixer, the rival, or the weakest player control of a consequential move. |
| The Crossover | The conflict retold without a game term, its practical cost, a human payoff within the chapter, a game-native detail that makes it more affecting | The recommending friend has to explain the channel or franchise first. Introduce the cost through visible action and delay unfamiliar terms. |

### 14.6 The resonance matrix
Report all five cohorts in one table, highest to lowest.

| Cohort | Score (of 20) | Dealbreaker triggered? | Resonance band | Strongest evidence (episode, timestamp) | Biggest gap |
|---|---|---|---|---|---|
| (each cohort) | | | | | |

**Resonance bands**

| Score | Band | Meaning |
|---|---|---|
| 16 to 20 | **Strong** | This cohort is likely to choose the show and come back for the next part |
| 11 to 15 | **Moderate** | They may sample it; a specific fix is needed for them to return |
| 6 to 10 | **Weak** | Occasional appeal, but the show rewards a different cohort's behavior |
| 0 to 5 | **None** | The show does not offer what this cohort comes for |

Also report the universal craft score (of 16). A craft score under 10 limits every cohort: no cohort can be rated above Moderate until craft issues are fixed.

**Reading the matrix**

- A show built for one cohort should score **Strong** for that cohort. High scores elsewhere are a bonus, never a substitute.
- If a different cohort outscores the declared primary, say so plainly: the show may be serving a different audience than intended. Recommend either revising toward the primary or re-declaring the primary.
- Two Strong cohorts that are neighbors (e.g., Lore Keepers and Scream Team) is healthy. Strong scores in opposed cohorts (e.g., Lobby and Drama Girls) usually mean two shows fighting inside one; check that neither payoff is diluted.
- A revision that raises a secondary cohort's score while lowering the primary's should be flagged as a trade-off, not recommended by default.

### 14.7 Verdicts (for the declared primary cohort)

- **Strong fit:** primary scores 16+, no dealbreaker, craft 10+.
- **Promising with revisions:** primary scores 11 to 15, or 16+ with a craft score under 10. Name the first revision likely to lift it.
- **Weak fit for the declared cohort:** primary scores 10 or below, or a dealbreaker is triggered. Report the best-fitting cohort separately.
- **Insufficient material:** too many signals are Unassessed to give a score. A transcript can support a story verdict while the audiovisual verdict stays open.

### 14.8 Return format, in order

1. Show, version, scope reviewed, declared (or inferred) primary cohort, and its promise.
2. **Resonance matrix** for all five cohorts, plus the universal craft score.
3. **Primary verdict** in one sentence, with inspection confidence tied to coverage ("pilot and finale reviewed, middle unavailable").
4. **Episode log** (one row per episode).
5. **Evidence by cohort:** every scorecard signal scored 1 or 2, with episode and timestamp; the strongest counterexample to the verdict.
6. **Revisions in priority order:** scene, change, which cohort it helps, which score it should lift, and what must survive the edit. Flag trade-offs between cohorts.
7. **Validation:** any real viewer data with its denominator and scope (or "unknown"); one matched comparison to run; the viewer behavior that would overturn the prediction.

### 14.9 Reusable resonance-test prompt
```
Using the bumpp Audience Intelligence Bible, run the Resonance test (Section 14)
on the attached show.
Declared primary cohort: [name, or "not declared"].
Score the universal craft criteria (14.4) and all five cohort scorecards
(3.14, 4.14, 5.14, 6.13, 7.9), citing episode and timestamp for every 1 or 2.
Apply dealbreakers, run the diagnostics in 14.5, and return the resonance matrix,
primary verdict, episode log, evidence, prioritized revisions, and validation test
in the order in 14.8.
Apply Section 12 safety rules and the Section 8.16 authenticity QA.
Mark anything you could not assess. Never invent timestamps, quotes, or reactions.
```

### 14.10 Example of an auditable finding
In the *Walden Academy* episode-one transcript, a social encounter becomes a distorted public account around 25:05 to 32:20 (reported by a parallel research review). For Lore Keepers this supports a score of 2 on signal 4 (witness logic). Captions and performance would be Unassessed from a transcript alone, and whether viewers returned because of this scene is unknown. One signal, one passage, not a series verdict.

---

# Appendices

## A1. Market and demographic foundation

### A1.1 Roblox: size, age, gender, geography

| Metric | Figure | Tag |
|---|---|---|
| Daily active users, Q3 2026 | 138 million (down 9% YoY, the first annual decline in company history; up 12% QoQ) | [D] |
| Hours engaged, Q3 2026 | ~34 billion | [D] |
| Age split of age-checked DAUs, 7 days ended Sept 30, 2026 | 34% under 13 · 37% aged 13 to 17 · 29% aged 18+ (Jan 2026: 35 / 38 / 27). Roblox calls these estimates from evolving methods. | [D] |
| 18+ share of age-checked DAUs, Q3 2026 | 29% globally · 37% in the US (up from 27% and 33% in Q2) | [D] |
| US teens 13 to 17 using Roblox daily | ~30% | [D] |
| US teens who use Roblox (Piper Sandler, Fall 2026) | 49% | [D] |
| Share of DAUs age-checked, end Q3 2026 | 64% globally; ~75% in US and UK; 80% in Australia | [D] |
| DAUs by region, Q3 2026 | APAC 42M · Rest of World 40M · Europe 32M · US & Canada 24M (Q2: 41 / 34 / 26 / 22) | [D] |
| Bookings by region, Q3 2026 | US & Canada $907M · Europe $360M · ROW $204M · APAC $226M | [D] |
| US adults 18 to 34, Q3 2026 | Daily users +26% YoY, +114% over two years | [D] |
| Fastest-growing markets, Q3 2026 YoY | India +37% · Japan +33% · Saudi Arabia +30% · Germany +13% · France +12% | [D] |
| Gender | Statista (Dec 2024): 52% male, 39% female, 9% unknown. Apptopia US mobile panel (Q2 2026): female weekly users passed male for the first time, growing 24% YoY vs 5% for males | [D] |
| Young adults (US mobile, 17 to 25) | Weekly users +20% YoY in Q2 2026; ~92 minutes per day per user in early Q3 2026 | [D] |
| Spending | US/Canada still generates over half of revenue despite ~18% of DAUs; adults monetize 50%+ more than under-18s | [D] |

**What this means for the engine** [I]

- The teen girl on mobile is the fastest-growing user on the platform in the US. She is our first viewer.
- Under-13 is a third of the platform and below our floor. Some will find us anyway (Appendix A1.5).
- The money sits in North America and with older users. The volume sits in APAC and Rest of World. Stories need to be legible in both.

### A1.2 Roblox's 2026 safety architecture (affects who sees what)

- **Age checks** (facial age estimation) became mandatory for chat in January 2026. Users without a check lose chat features. [D]
- **Roblox Kids (ages 5 to 8) and Roblox Select (ages 9 to 15)** launched globally on June 16, 2026. Select accounts can access games rated up to Moderate that pass Roblox's selection process. Users move to standard accounts at 16. [D]
- **Implication** [I]: anything we stage inside a game rated above Moderate will not be explorable in-game by 13 to 15 spillover viewers. Our 16+ core is unaffected. If a show is meant to drive viewers into a companion map or event, keep that map at Moderate or below.

### A1.3 Minecraft (secondary platform)
Minecraft data is weaker than Roblox data. Microsoft has not published an official monthly-player figure since 2020 (~126 million). Aggregators estimate 200 million+ monthly players in 2025 to 2026, with roughly 43% aged 15 to 21 and a male skew around 54%, but treat those as directional only. [D, low confidence]

The most useful number: research cited by Jonathan Haidt's After Babel estimates Minecraft and Fortnite each draw roughly 30 million monthly users under 18, against roughly 305 million under-18 monthly users for Roblox. [D]

**What this means** [I]

- Minecraft is a boy-leaning, slightly older, lore-and-SMP culture (servers, factions, long-running "lore" arcs, Hardcore challenges). Its storytelling heritage runs through machinima like *Parkour Civilization* (45M+ YouTube views) and SMP lore, not through teen-girl romance drama.
- Minecraft fits Cohort 3 (horror, mystery) and Cohort 4 (adventure, comedy, lore) better than Cohort 1.
- [K] A Minecraft Movie (2025) was one of the biggest films of its year and turned "chicken jockey" into a theater-shouting meme; a sequel is dated for 2027. Verify before citing externally.

### A1.4 Age: is 14 to 18 the sweet spot? (the brief asked us to double-check)

**Short answer: the existing fandom's sweet spot is 14 to 17, but bumpp targets 16 to 19 as its core, 20 to 24 as its ascending audience, and writes characters 17 to 21.** The evidence below explains the existing audience; Section 2.1 explains the decision to aim older.

The evidence:

- 37% of age-checked Roblox users are 13 to 17, the single largest band (Q3 2026). [D]
- Girls' gaming drops with age: 81% of US girls 13 to 14 play video games vs 67% of girls 15 to 17 (Appendix A1.7). [D]
- Piper Sandler's teen panel averages 15.7 years old (Fall 2025) and shows Roblox usage at 49% in Fall 2026, up from roughly 47% a year earlier, which Piper called a record at the time. [D]
- The creators making the genre's biggest hits are themselves teens. The Walden Academy creator lists her age as 17 on her channel. A Roblox film director profiled in late 2025 was 17; another was 20 and another 22. [O][D]
- Comments, fan accounts, and fan pages around these shows use high-school framing (school, "moots," prediction posts, ship wars). [O]
- The North Star bets on 16 to 22 as the commercial core. Older Roblox users are the fastest-growing segment and monetize 50%+ better. [D][NS]
- Teens watch up. Content about 17-year-olds is aspirational to 14-year-olds; content about 14-year-olds is a turn-off to 17-year-olds. [I, standard in youth media but test it]

**Recommendation** [I]

| Layer | Ages | Role |
|---|---|---|
| Protagonist age | 17 to 21 (senior year, gap year, college, first job, moving out) | Aspirational for 15 to 18, relatable for 18 to 22 |
| Core viewer | 16 to 19 | Fandom energy plus growing spend; the design target |
| Ascending viewer | 20 to 24 | Spend, sharing to wider networks, crossover with K-drama and microdrama apps |
| Spillover viewer | 13 to 15 | Will watch regardless. Not a design target, but a safety constraint (Section 12) |

### A1.5 The spillover problem
Younger teens (13 to 15) will watch content aimed at 16 to 19, and under-13s (about a third of Roblox) will try to, despite our 13+ floor. [D][I] Two consequences:

1. **Write for 18, not for 14,** but never write anything you would not want a 13-year-old to see. That is the practical ceiling.
2. **YouTube "made for kids" risk** [K]: if YouTube or a regulator treats a channel as child-directed, comments, notifications, and personalized ads switch off. Comments and community features are the genre's lifeblood. Channel positioning, thumbnails, and titles should read as teen-directed, not child-directed. Legal should review.

### A1.6 How teens consume video (the bigger media diet)

| Signal | Figure | Tag |
|---|---|---|
| Favorite social app, US teens (Fall 2026) | TikTok 48% · Instagram 31% · Snapchat losing share | [D] |
| Share of daily video time (Fall 2026) | YouTube and Netflix tied at 28% each | [D] |
| Teens "almost constantly" on TikTok or YouTube | About 1 in 5 | [D] |
| Teens online "almost constantly" | 46% | [D] |
| Teens using YouTube daily | ~73% | [D] |
| Gender pattern | Girls slightly more likely to be on TikTok and Instagram almost constantly; boys more likely on YouTube | [D] |
| AI chatbot use, US teens | 64% use chatbots; ChatGPT used by 66% in Piper's panel | [D] |
| Microdrama viewing | 35% of Gen Z (13 to 24) watch microdramas vs 22% of all consumers | [D] |
| Microdrama market | ~$11B globally in 2025, projected ~$14B in 2026 | [D] |
| Microdrama audience shift | Getting younger and more male; viewers 22 to 27 nearly tripled their share on My Drama over five quarters | [D] |
| Where a "story" can live, per teens | YouTube (72.9%), TV (70.3%), movies (70.2%), video games (68.5%), TikTok (64.2%), AI (41.3%) | [D] |
| Live action vs animation preference | 58% vs 42% in 2026, live action regaining the lead | [D] |
| Casting preference | ~40% would cast an unknown actor; 16.8% would cast an influencer | [D] |
| Weekend activity #1, three years running | Seeing a new movie in a theater | [D] |

**What this means** [I]

- Distribution is YouTube for long-form episodes, TikTok and Shorts for discovery clips, edits, and auditions, and Discord for the core community. bumpp's own app must earn its place alongside those, not replace them.
- "Animated avatars" are not automatically a liability. The audience treats Roblox drama as its own medium. But the live-action rebound and the "unknown actor" preference say: make characters feel like real people with real interiority, not mascots.

### A1.7 Reaching the 16+ girl: she may watch more than she plays
This is the most important blind spot in the decision to aim older. The evidence says gaming drops off for older teen girls, so the 16 to 19 core will often be reached through drama habits rather than game habits.

- Among US teens, 81% of girls aged 13 to 14 play video games versus 67% of girls aged 15 to 17; nearly all boys play regardless of age. Only 17% of teen girls call themselves "gamers," against 62% of boys. Overall, 85% of teens play but only about 40% identify as gamers. [D] (Pew, survey fielded Sept to Oct 2023)
- In UK data, Roblox time decreases with age while TikTok time increases (Ofcom passive measurement of 8 to 14s). [D] A parallel research brief reports Ofcom survey figures of 51% recent Roblox use among 8 to 14s versus 26% among 15 to 17s. [P]
- Roblox's own growth is coming from adults: US users aged 18 to 34 grew 26% year over year in daily users in Q3 2026. [D]

**What this means** [I]

- Do not assume our 16 to 19 viewer opens Roblox daily. She may know the visual language from years of play and now consume mainly through YouTube, TikTok, and edits.
- Never write characters or packaging that require gamer identity. Most players, especially girls, don't claim it.
- Cohort 2 (Drama Girls) and the clip-first entry route (Appendix A3, Circle 4) matter more under the older target than they did under the 14 to 17 framing.

### A1.8 Platform shifts worth tracking (Q3 2026) [D]

- **Moments:** Roblox is bringing off-platform-style video into the Roblox app, live across most of the US, with commenting and direct avatar-item purchasing from videos. This is both a potential distribution surface and a direct fashion-commerce path for show wardrobes. Watch it closely.
- **Web Play:** games will be joinable from a link in a browser (Chrome first), so a link in a YouTube description or a DM can drop a viewer straight into a companion game.
- **Classmates:** launched November 18, 2026 for US college students, with Roblox clubs reported at over 100 colleges across 30 states. Club founders describe it as a remedy for campus isolation, especially for commuters.
- **Age-check caveat:** Roblox notes its age-checked metrics are estimates from evolving methods and may not represent the whole platform. Treat all age splits in this file as directional.

## A2. The genre as it exists today: "Rollywood"

### A2.1 What it is
Long-form scripted series, movies, and Shorts staged inside Roblox games, voiced by players, edited like television, and released on YouTube with TikTok promotion and Discord communities behind them. A December 2025 profile described the format as 20 to 30 minute episodic releases or "movies" running past two hours, mostly made by teens, staged largely in **Berry Avenue** (a realistic life-sim map), with promo posters, trailers, mock MPA-style age ratings, and YouTube premiere nights. [D]

The scene has three production tiers [O]:

1. **Cinematic studios.** Moon Animator, custom maps, camera rigs, foley, multiple voice takes. Example: Robuilds' 78-minute film *Susan*, made with 100+ volunteers. The format's all-time reference is ObliviousHD's *The Last Guest* (95M+ views).
2. **Serialized drama studios.** Berry Avenue series with open casting, Discord ops, cast promotion. Examples: Noiré Studios (Walden Academy), Selvienne Productions (Finders Keepers), Reverie Productions (AMATEURS), novasfilms (The Shift).
3. **High-velocity hook channels.** Single-creator, ALL-CAPS titles, "POV" and "I became..." formats, Shorts-first. Example: stinkella.

Adjacent formats [O]:

- **Family roleplay sitcoms** ("morning routine," "night routine," "billionaire family") such as The Roblox Rebels and Elyxia. Skews younger.
- **Live theater in Roblox:** Illumination Theatre staged *Hamilton* live in its own Roblox game (it moved out of Bloxburg in August 2026), followed by *Shrek the Musical* auditions and *Dancing with the Illuminators*, a weekly vote-for-your-couple competition.
- **Reality parodies:** *Crush Island* (a Love Island parody by Elyxia) is cited as one of the genre's sharper pieces. [D]

### A2.2 Reference studio teardown (data pulled Nov 21, 2026) [O]

**Noiré Studios · @adoreesydd · Walden Academy** (165K subscribers; creator self-describes as 17)
Berry Avenue boarding-school drama. Prior series: *Vendetta* (two powerful families, decades-long feud, hidden fortune; ~160K to 184K views per late episode).

| Episode | Title | Released (UTC) | Views |
|---|---|---|---|
| Prologue | "Scholarship" | Dec 6, 2025 | 299,734 |
| Ep 1 | "Poison Ivy" | Dec 25, 2025 | 1,540,899 |
| Ep 2 | "Terms & Conditions" | Jan 15, 2026 | 680,199 |
| Ep 3 | "Mind Your Manners" | Feb 25, 2026 | 558,923 |
| Ep 4 | "Winter is Coming" | May 15, 2026 | 443,074 |
| Ep 5 | "Kiss and Tell" | Jun 7, 2026 | 349,891 |
| Ep 6 | "Trick or Truth" | Jul 6, 2026 | 290,838 |
| Ep 7 | "Social Currency" | Jul 24, 2026 | 282,421 |

What it does right:

- **Premise:** scholarship kid enters an elite academy. Class collision is the engine. Fans compare it to *Gossip Girl* in their own theory posts.
- **Named, ship-able leads:** Blaire Patridge, Roman Grimaldi, Dain Buchanon. Fans coined the ship name "Romaire." Fan tags lean "enemies to lovers."
- **Episode titles are idioms with a double meaning.** Short, quotable, social.
- **Holiday launch:** Episode 1 premiered on Christmas Eve night, US time. Holiday downtime plus new-device time. [I on causation]
- **A full ecosystem:** cast Q&A videos, a debrief podcast called "Walden Academy After Hours," a "How to Make a Berry Avenue Series" filmmaking tutorial (86K views), open auditions posted to TikTok with a branded hashtag, Discord-run casting, fan edit accounts (e.g., @adoree.walden), Pinterest boards, prediction and theory posts.
- **Episode 1 to Episode 7 retention: ~18% of Ep 1 views.** Gaps of 3 to 12 weeks between episodes.

**Selvienne Productions · Finders Keepers** (10.5K subscribers)
Ep 1: 156,220 · Ep 2: 58,749 · Ep 3: 39,334 · Ep 4: 31,607 · Ep 5: 23,211. Ep 5 is ~15% of Ep 1. Trailer released after Ep 3 drew 10,866. Next project: "THE BLUR."

**Reverie Productions · @xoetherealuv · AMATEURS** (24.2K subscribers)
A Berry Avenue *modeling* series. Ep 4: 77,567 · Ep 5: 73,049 · Ep 6: 80,529 · Ep 7: 39,496 (one week old). Notably flat mid-season retention, which is rare. Extras: "AMATEURS Cast Plays 'Sip or Spill'" interview (23,684), spoiler drops during production breaks, auditions reopened between seasons, and a utility video ("BERRY AVENUE DYNAMIC HEADS FIX," 23,792). [O] The user's brief also named *Strings Attached* from this creator; it did not appear in the recent feed.

**novasfilms · The Shift** (sci-fi)
Ep 1 "Doomsday": 158,970 · Ep 2 "Strangers": 63,157 · Ep 3 "Familiar Faces": 42,653 · Ep 4 "The Trials" (Season 1 finale): 26,801. Promos: teaser trailer, open casting call, a "Ghost Face" horror skit, "Cooking With CASTS!" Teaser cut to a SZA track.

**Illumination Theatre** (9.97K subscribers)
YouTube views are small (*Hamilton in ROBLOX Pro-Shot*: 5,478). The product is the live in-game event and the Discord community, not the upload. Recruitment runs entirely through Discord auditions. [O]

**stinkella / "stink studios"** (606K subscribers)

| Title | Views |
|---|---|
| He called me UGLY, so I became a CAMISA BADDIE... | 5,564,131 |
| The Royal PRINCE is LOCKED in my Dorm Room... \| Royal Assistant Ep. 1 | 1,253,133 |
| CAUGHT My Boyfriend CHEATING with my FRIEND 💔😢 | 918,459 |
| I NEED THESE PEOPLE FOR MY NEXT ROBLOX STORY… 🎬 | 770,598 |
| Valentina Tutorial (CAMISA BADDIE) | 404,244 |
| MY ROBLOX CHEER RPS ARE CRAZY… (#euphoria #cheer) | 351,209 |
| POV: You go to VALEWOOD University 💸💰💎✨ | 351,915 |
| HOW TO REMOVE DYNAMIC HEAD ANIMATION | 217,375 |

What it teaches:

- **The glow-up revenge hook is the single biggest title in the sample.** Humiliation, transformation, payback. Classic microdrama logic, executed natively.
- **Royalty, wealth, and elite schools recur** (Royal Assistant, Valewood University, "richest school in the world").
- **The outfit tutorial for a character's look ("Valentina Tutorial") pulls 400K views on its own.** The character's look is a product. [O] This is the Blueberry bridge (Section 9.4).
- **Casting calls are content** (770K views for "I need these people for my next Roblox story").
- **Technical tutorials (dynamic heads) are content.** Facial animation matters to the audience.

**The Roblox Rebels · Billionaire Family series** (reality / family RP)
"WE MOVED INTO A MILLION DOLLAR MANSION! *NEW SERIES*," "BILLIONAIRE GIRLS TRY OUT FOR THE CHEER TEAM!," morning and night "routine" videos. 3K to 12K views per episode in late 2024. Younger audience, wish-fulfillment wealth fantasy, voiced. [O]

**Not verified:** *Crucible* by @RevolutionizedStudio could not be retrieved in this pass. Add when available.

### A2.3 Patterns across the sample [O][I]

1. **Episode decay of 80% to 85% from Ep 1 to Ep 5 to 7 is normal.** The best-retaining show (AMATEURS) has a narrow premise (modeling competition), a clear weekly-ish cadence, and between-episode content.
2. **Berry Avenue is the dominant set.** It is a studio lot, not a destination: only ~44K to 48K people are playing it at any moment in Nov 2026, against 400K+ in Brookhaven. Viewers of Berry Avenue dramas are not necessarily Berry Avenue players. [D][I]
3. **Premises cluster around status:** scholarship vs. elite, maid vs. heir, ugly vs. baddie, new girl vs. queen bee, rival families, royal and commoner.
4. **Titles in the high-velocity tier** use CAPS, ellipses, "POV," "I became," "I got caught," plus emoji. Titles in the prestige tier use the series name, episode number, and a short ironic idiom in quotes.
5. **Fans participate in production.** Auditions are public, cast lists are announced, extras are recruited. The audience wants in.
6. **Long gaps kill momentum.** Every show in the sample had gaps of several weeks. A studio that can ship weekly has a structural advantage. AI-assisted production is the lever here. [I]

### A2.4 Additional references from the parallel pass [P]

| Reference | What to study | Link |
|---|---|---|
| *Strings Attached* (Roblox) | Work forces two people with an uncomfortable past together (around 8:15 to 9:32 of the first episode). Would viewers stay for the professional partnership if the romance vanished? | https://www.youtube.com/watch?v=UL-6U0vITDg |
| *Royal Assistant* (Roblox, stinkella) | An object warning set up early pays off late in episode one. Note: the parallel pass flagged coercive material in the source; do not replicate it. | https://www.youtube.com/watch?v=LfvBIxROvqE |
| *Walden Academy* Ep 1 | An encounter becomes a distorted public account (around 25:05 to 32:20). Give three people different access to one event. A parallel review of 20 top comments on this episode coded most reactions as dialogue humor, theories, and streaming comparisons (log not supplied to us). | https://www.youtube.com/watch?v=n2Cn9n3In-g |
| *Hermitcraft*, *Third Life*, *Unstable* (FlameFrags), Aphmau roleplays (Minecraft) | Accumulated place, multiple creator POVs of one event, staged collaborative storytelling. Does the attraction survive a different creator? | https://blog.youtube/culture-and-trends/minecraft-15/ |
| Spanish-language Brookhaven stories (e.g., Celynnei, Las Nievecitas) | Doubles, zombies, and suspense in a familiar neighborhood. Evidence of Spanish-language supply, not viewer demographics. | https://socialdiscovery.app/es/youtube/themes/gaming/sandbox-games/roblox?page=2 |
| *Evermore High* and *Cat Battles* (Roblox, Nov 2026 showcase) | A social-school game whose creator names girls and young women as the intended audience, next to a physics comedy. Two different routes into group entertainment. | https://about.roblox.com/newsroom/2026/11/new-standout-games-to-check-out-on-roblox-this-month |
| *Parkour Civilization* (Evbo, Minecraft) | A spatial obstacle makes status visible to a newcomer; a device that transfers to original Roblox settings. | https://www.youtube.com/watch?v=2pFwQiwRbcg |

### A2.5 Reading public view counts correctly [P][I]
The episode decay figures in 3.2 compare public view totals across episodes. That is a useful signal about discovery and continuity, but it is **not** same-viewer retention: later episodes have had less time to circulate and may reach different people. YouTube's retention chart measures behavior within a single video. To know whether the same people came back, use a consistent follow-up window on the same eligible viewers (channel analytics) or a consented choice test.

## A3. A second axis: how close is someone to the format?

The five named cohorts in Section 2.2 describe **what brings people back** (romance and rivalry, horror, comedy, and so on). This section adds a second axis from a parallel research pass: **how close someone already is to watching scripted stories filmed inside games.** Use both. A viewer gets one named cohort (motive) and one circle (distance). [P][I]

### A3.1 What counts as resonance
Someone chooses an unfamiliar show, understands the first consequential choice, and **voluntarily comes back for the people or the unresolved question.** Recognizing a game thumbnail, completing one clip, and returning for part two are different outcomes. bumpp optimizes for the last one. [P]

### A3.2 The five circles (cumulative; assign each person to the earliest matching circle)

| Circle | Who is added | Behavior that qualifies them | What the show must earn |
|---|---|---|---|
| 1 | Returning viewers of serialized Roblox roleplay and character drama | Came back unprompted and can explain a relationship that changed | Loyalty to an unfamiliar cast |
| 2 | Followers of other serialized game worlds, including Minecraft story and lore fans | Follows a server, creator story, horror mystery, or alternate POV across uploads | Trust that this Roblox world has rules worth following |
| 3 | Social players, builders, and roleplayers who rarely watch filmed series | Can recount something their group made, decided, or argued about | A reason to watch when they could play |
| 4 | Short-drama and fandom-clip viewers without game-story habits | Saves a reveal, seeks part two, watches a recap, or sends a scene to someone | A readable first scene and a satisfying second click |
| 5 | Broader gamers, animation and genre fans, lapsed players, friends invited along | Accepts a recommendation on the strength of a human dilemma, a scare, a joke, or an event | A story that works on first contact with the game |

The unit is a viewing habit, not a personality type. A former player can sit in Circle 1. A daily player can sit in Circle 5. [P]

### A3.3 Mapping the named cohorts to the circles [P][I]

| Named cohort | Usual circles | What they want to do with the story | What loses them |
|---|---|---|---|
| Lore Keepers | 1 (Roblox casts), 2 (Minecraft and other worlds) | Remember a promise, notice who broke it, compare accounts with a friend. An old key still opening a door says more than a narrator explaining the old friendship. | A reset that erases last week's cost, or a reveal with no earlier clue |
| Drama Girls | 1 (regular Roblox drama viewers), 4 (arriving from edits, romance serials, webtoons) | See a guarded person choose sides in front of someone whose opinion matters. Fake dating, second chances, rival partners as entry points. Viewers of any gender can qualify. | A love interest with no ambition, a triangle that only works because nobody asks the obvious question, humiliation sold as affection |
| Scream Team | 1 or 2 (already follow game horror), 3 (play it with friends), 5 (genre-first newcomers) | One viewer pauses for background evidence; another wants the shared moment of realizing the safe room changed. A consistent rule, a visible breach, a person worth warning. | A loud sound that resolves everything, a clue unreadable on a phone, suffering with no consequence |
| The Lobby | Usually 3; sometimes 2 when a group rivalry becomes a season | Decide whether the team made the right call. A funny failure or a public refusal to take an unfair advantage travels back to their own group chat. | Characters explaining a game everyone would rather play, a win that costs nobody anything |
| The Crossover | 4 (a clip starts it), 5 (a friend or genre is the reason) | Follow a legible human problem immediately, before learning any game term | A channel in-joke in the opening, a lore glossary, a teen setting pasted onto supposedly independent adults |

### A3.4 Gender: lead with demonstrated affinity, not assumption [D][P][I]

- Holywater's 2026 microdrama report finds the vertical-drama audience getting younger **and more male**. [D]
- In an April 2026 Dentsu panel of US and Canadian adults, 28% of men and 18% of women met its microdrama viewer definition (adults only, all microdramas). [P]
- The Roblox-drama genre's fan reactions are character- and relationship-driven, but its audience gender mix is unmeasured. [O]

**Rule:** keep three variables separate in every test: the lead's gender, the viewer's gender, and genre preference. Do not hand every girl a romance and every boy a horror show. Girl-led stories should appear across mystery, team rivalry, horror, and friendship, not only romance.

---

## B1. Open questions and data gaps (do primary research before scaling)

1. **The legacy brand guide** did not come through in this thread. The parallel pass had the June 2025 Blueberry fashion guide and reports it was used for historical brand context only, with no audience finding depending on it. Fold in its audience material if any exists.
2. **Crucible by Revolutionized Studio** could not be retrieved; add a teardown. *Strings Attached* now has a reference entry (A2.4) but no full viewing audit. *Finders Keepers* and *The Shift* also lack scene-level audits.
3. **Minecraft audience data** is weak (no official MAU since 2020). Commission a small survey or pull data from partner Minecraft creators before committing more than one or two Minecraft shows.
4. **Gender split of Roblox-drama viewers** is inferred, not measured. Ask partner creators for YouTube Analytics (age, gender, geography, retention curves) under NDA.
5. **International viewership** of English-language Roblox series is unmeasured. Test subtitled vs. dubbed releases in two markets.
6. **Vertical vs. long-form** for this audience: test the same show in both formats.
7. **Retention drivers:** pull audience-retention graphs (not just views) for 10 to 20 episodes across studios to locate exact drop points.
8. **Build a paid youth reader panel** (16 to 22, international, consented, with parental consent for minors) to run the Section 8.16 QA on scripts and refresh the slang shelf every month.
9. **Run 15 to 20 Discord interviews** with Cohort 1 viewers (with parental consent where minors are involved) and 10 with Cohort 2 and Cohort 3 viewers.
10. **Licensing pathway** for Berry Avenue or an owned set strategy.
11. **Re-verify all [K] items** before external use.

**Refresh cadence:** slang (Section 8.6) and texting conventions (Section 8.4) monthly; culture map (Section 9) quarterly; demographics (Appendix A1) after each Roblox earnings release.

## B2. Validation plan: how we learn whether this file is wrong [P][I]

1. **Recruit on behavior before taste labels.** Ask for the last game-filmed story watched, how it was found, what happened, whether they chose another part, what they abandoned, and what they watched instead. Log play frequency, viewing language, age, and voluntarily described gender separately. Include quiet watchers, nonplayers, and game-literate skeptics. Compare college students with same-age nonstudents. Use age-appropriate recruitment, parental consent for minors, and de-identified reporting.
2. **Age cells:** 13, 14 to 15, 16 to 17, 18, 19, and 20 to 24. This tests both the original 14 to 18 hypothesis and the 16+ decision without merging them.
3. **Compare like with like.** Randomize concept order; hold production quality, title clarity, and exposure constant. Cross genre with age and gender instead of matching romance to girls and horror to boys. Rotate matched short and long versions.
4. **Measure the decision that matters, as four separate numbers:** first choice per exposed viewer; correct unaided explanation of the key choice; deliberate selection of the next part per eligible viewer; voluntary return over a fixed follow-up window. Also track sound-off comprehension, title recall, and how many would rather play.
5. **Let contrary evidence change the brief.** If younger or older cells return more than 16 to 19 after matching viewing habits and exposure, revisit the target. If girls click more but return at the same rate, fix packaging before claiming a gender preference. If Minecraft lore viewers outperform Circle 1 on unfamiliar casts, elevate them. If a local voice track reverses a ranking, keep a market-specific ranking.
6. **Keep the evidence hierarchy.** Representative research describes its stated population; creator analytics describe an actual channel; comments and interviews suggest motives; choice tests compare specific treatments. A creator's intended audience, an avatar's look, search volume, or an AI-generated persona never establishes who actually watches.
7. **Interview script for replacing invented persona details with evidence:** reconstruct yesterday after school or work; the last weekend they enjoyed; the last scene they sent, to whom, and what else they talked about; the last optional purchase made or skipped, its cost in local currency, who chose it, and who paid. Report ranges and the share spending zero alongside any median.

**Outcome definitions (use these denominators)** [P]

| Outcome | Denominator and interpretation |
|---|---|
| First choice | People choosing this option ÷ people exposed to comparable options. Randomize order; note when an invitation or known creator drove the click. |
| Unaided comprehension | Among viewers who saw the scene, ask what changed and for whom, and code it before revealing the intended payoff. A surprising but text-supported reading can be a creative success. |
| Next chapter | Of viewers given the same real opportunity, how many chose the follow-up (with a real alternative and the option to stop). "Would watch" is self-report, not this. |
| Voluntary return | Of eligible earlier viewers with the same opportunity and window, how many actually came back. State window, sample, reminders, visibility of the next episode, and missing data. |
| Cross-cohort or cross-market difference | Compare similar exposure, language, creator affinity, and play habits; show numerators, denominators, and uncertainty. No population rankings from small cells. |

## B3. Blind spots that could change the brief [P]

| Missing perspective or confound | Why the engine could misread it | How to resolve it |
|---|---|---|
| Private watchers who rarely comment or buy | Public fandom makes the most expressive viewers look like everyone | Recruit beyond creator channels; compare quiet viewers with posters |
| Followers of a performer, editor, soundtrack, or game update | A familiar face or song can explain the first click even when the characters have little pull | Compare familiar and unfamiliar casts; ask what they'd still watch with the creator or music swapped |
| Edge ages and young adults outside college | "Gen Z" averages hide employment, school stage, spending authority, and who can watch at home | Use the same stories across ages 13, 14 to 15, 16 to 17, 18, 19, 20 to 24; include nonstudents, working students, caregivers, free-only viewers |
| Disabled, neurodivergent, multilingual, and shared-device viewers | A missing caption or costly connection looks like disinterest in the genre | Test captions, sound access, and real device conditions; fix barriers before reading rejection as creative |
| Gender, cultural identity, family structure | People can share a viewing habit and disagree about a pairing; background alone predicts little about voice or genre | Vary leads across genres; recruit on viewing behavior; keep small-group results private |
| Short-only fans and people who'd rather play | A clip or a game can be a complete pleasure; completion can coexist with no demand for a series | Offer another chapter, a different clip, a play option, and the option to leave; judge each format on its own promise |
| Samples from one English-speaking city | A Manila convenience sample can't speak for the Philippines or APAC; a US-only campaign makes the US look more naturally drawn | Label recruitment, place, campaign, age, language, device; compare matched local cuts |
| Dated media, slang, and listings | Old favorites can be enduring, ironic, or unknown | Keep date, population, and inspection scope beside every reference; refresh before production |

---

## C. Sources

**Internal**

- bumpp Branding and North Star (May 2026, Google Drive) and bumpp × boopp Brand Supplement v4 (June 2026). [NS]

**Roblox company data and safety**

- Roblox Q3 2026 earnings coverage: gaming.net, GamesBeat, MarketBeat call highlights, GGRecon (Oct 30 to Nov 2, 2026). https://gaming.net/roblox-q3-revenue-rises-16-as-bookings-fall-12-to-1-7-billion · https://www.marketbeat.com/instant-alerts/transcript-roblox-q3-earnings-call-highlights-2026-10-31/ · https://www.ggrecon.com/articles/roblox-daily-players-fall-q3-2026/
- Roblox Q2 2026 regional DAUs: PocketGamer.biz. https://www.pocketgamer.biz/roblox-revenue-rises-36-yy-but-young-north-americans-see-falling-per-hour-monetisation/
- Roblox Q1 2026 call transcript (18+ hours growth by country): Benzinga. https://www.benzinga.com/insights/news/26/04/52200813/roblox-q1-2026-earnings-call-complete-transcript
- Age split 35/38/27 of age-checked users (Jan 2026), as reported by secondary trackers citing Roblox. https://www.shanethegamer.com/research/roblox-statistics/
- Roblox Kids and Roblox Select accounts: Roblox Newsroom (Apr 2026) and Business Wire (Jun 16, 2026). https://about.roblox.com/newsroom/2026/04/introducing-roblox-kids-and-select-accounts · https://www.businesswire.com/news/home/20260616748440/en/
- Apptopia, "Female WAUs Now Outnumber Male WAUs on Roblox Mobile" (Jul 28, 2026). https://apptopia.com/en/insights/female-waus-now-outnumber-male-users-on-roblox-mobile/
- Statista gender split (Dec 2024), via DemandSage. https://www.demandsage.com/how-many-people-play-roblox/
- Roy Morgan, Young Australians Survey on Roblox (Mar 2026). https://www.roymorgan.com/findings/10136-yas-roblox-for-young-australians-survey-december-2025
- Live concurrent players (Nov 2026): rblxdb, statroblox, livecounts. https://rblxdb.com/roblox-player-count · https://statroblox.com/leaderboards/playing
- Wikipedia: List of Roblox games; Steal a Brainrot.

**Minecraft**

- SQ Magazine, DemandSage, Search Logistics aggregator estimates (low confidence). https://sqmagazine.co.uk/minecraft-statistics/
- After Babel estimates of under-18 MAU by platform, via Cal Newport. https://calnewport.com/whats-worrying-jonathan-haidt-now

**Teen media behavior**

- Piper Sandler Taking Stock With Teens, Fall 2026 (coverage: Investing.com, Seeking Alpha, Walter Bloomberg on X) and Fall 2025 (Piper Sandler release). https://www.investing.com/news/analyst-ratings/piper-sandler-teen-survey-shows-beauty-spending-rises-tiktok-gains-93CH-4947072 · https://www.pipersandler.com/news/piper-sandler-completes-50th-semi-annual-teen-survey
- Pew Research Center, "Teens, Social Media and AI Chatbots 2025" (Dec 9, 2025). https://www.pewresearch.org/internet/2025/12/09/teens-social-media-and-ai-chatbots-2025/
- UCLA Center for Scholars & Storytellers, Teens and Screens 2026, "Rewrite This!" (Oct 21, 2026). https://newsroom.ucla.edu/releases/annual-teens-screens-report-reveals-young-audiences-redefining-modern-storytelling
- UCLA CSS Teens and Screens 2025 coverage (SheKnows, PinkNews).
- Child Mind Institute, Building Bridges: Teen Loneliness and Connection (Oct 2026). https://www.morganstanley.com/insights/articles/child-mind-institute-study-2026
- AEI 2026 American Teenagers Survey coverage; Brookings on school phone bans (2026); Talker Research / Aura teen stress survey (2026).

**Microdrama**

- Omdia figures via eMarketer and Quartz; Hub "Video Redefined" via Señal News; Holywater × Owl & Co "State of Microdrama 2026"; Media Partners Asia ReelShort report; Apptopia microdrama share. https://www.emarketer.com/content/faq-on-microdramas--mobile-video-format-outpacing-netflix-daily-engagement · https://senalnews.com/en/data/vertical-series-global-market-heads-for-150-billion-in-2026

**Horror box office**

- Screen Daily, The Playlist, NPR/Fresh Air, Fox News, ComingSoon (May to Jun 2026) on Backrooms and Obsession. https://www.screendaily.com/news/youtube-creators-rule-us-box-office-backrooms-opens-on-a24-record-82m-obsession-hits-100m/5217268.article

**The Roblox drama scene**

- Kieran Press-Reynolds, "The Scandals, Chaos, & Next-Gen Soap Operas of Roblox-Hollywood," mixed feelings (Dec 3, 2025). https://www.mixedfeelings.earth/p/inside-the-scandalous-world-of-roblox-tv-film-machinima-berry-avenue
- Channel RSS feeds and pages pulled Nov 21, 2026: @adoreesydd, @selvienneproductions, @xoetherealuv, @IlluminationTheatre, @novasfilms.x, @stinkella, The Roblox Rebels playlist.
- TikTok captions and tags for #waldenacademy and #waldenacademyberryave; Noiré Studios Roblox group description.

**Slang**

- Mental Floss (Sep 2026), genppt (Oct 2026), Made For Mums (Nov 2026), Kid Inspector, Slangwise, Talking Pretty.

**Texting, emoji, and slang origins**

- UCLA Language in Life project on Gen Z punctuation and emoji; SheKnows teen interviews; CNN/Adobe emoji study; The Star (Kenya, Jul 2026); unanswered.io and CleverType 2026 texting guides.
- NBC News, "Appreciation or appropriation? How Black culture is shaping Gen Z slang"; Business Insider/Yahoo on Gen Z slang origins; U-High Midway (Jan 2026).
- Roblox RP glossaries (AxeeTech 2026, Bloxodes, community RP wikis).

**Roblox, Pew, Ampere, Ofcom coverage (verified)**

- Roblox Q3 2026 Shareholder Letter (SEC Exhibit 99.1) and Q3 2026 Investor Data Sheet. https://www.sec.gov/Archives/edgar/data/1315098/000162828026068235/ex991-q32026earningsshar.htm · https://s27.q4cdn.com/984876518/files/content_files/Q3-2026-Investor-Data-Sheet.pdf
- Roblox, "Introducing Classmates" (Nov 18, 2026). https://about.roblox.com/newsroom/2026/11/introducing-classmates-a-new-way-for-us-college-students-to-connect-on-roblox
- Pew Research Center, "Teens and Video Games Today" (May 2024; fieldwork Sept to Oct 2023). https://www.pewresearch.org/internet/2024/05/09/teens-and-video-games-today/
- Ampere Analysis mini-drama study (Oct 2025), via Broadband TV News, Advanced Television, World Screen.
- Ofcom passive measurement coverage (PocketGamer.biz, 2026).

**Philippines and additional references**

- Philippine Statistics Authority and DICT, 2024 National ICT Household Survey (verified via Sunstar, Insider PH, PTV News coverage, July 2025).
- From the parallel pass [P]: Education Week teacher survey on student slang (July 2026); ABS-CBN on *He's Into Her*; Netflix on *All of Us Are Dead*; W3C media accessibility guidance; UCLA CSS 2026 gaming pull-out.

**From the parallel research pass [P] (not independently re-verified)**

- Ofcom Children and Parents Media Use and Attitudes 2026; Dentsu Consumer Navigator April 2026; OECD PISA 2022 vol. IV; BLS CPS 2025; Common Sense Media 2026 census; Gambling Commission/Ipsos 2025 youth leisure tables; SMBC Consumer Finance 2024; Cetic.br TIC Kids Online Brasil 2025; Kidscorp Brazil 2025; JIM 2025 (Germany); Mynavi Teens Lab 2026; YTJP Sept 2026; Teacher Tapp Aug 2026; Oxford Children's Word of the Year 2025; Pew teen social media and mental health (Apr 2025); Roblox Replay 2025; YouTube Minecraft and Roblox retrospectives; UCLA CSS 2025 report and 2026 gaming pull-out.

**Romance tropes**

- Automateed (2026), Book Riot BookTok YA 2026, The Citizen on Gen Alpha "swoon without the spice," Wattpad head of content interview (Her Campus).
