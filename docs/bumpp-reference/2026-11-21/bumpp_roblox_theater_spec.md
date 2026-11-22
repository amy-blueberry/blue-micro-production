# bumpp on Roblox: The Theater Park
### Product spec and build brief for Ali

Prepared Nov 21, 2026 · Internal / Confidential · Owner: Amy
Working title: **bumpp Cinema** (placeholder; naming is open)

---

## 0. Read this first

**What we're building:** a Roblox game where bumpp shows play inside a theme park built around them. You walk in, get rewarded right away, watch an episode with friends, then everything around the episode turns into play: collecting, dressing up as the cast, trivia, predictions, recreating scenes, and buying the outfits the characters wear.

**Why:** people aren't downloading the bumpp app. Asking a Roblox kid to install a new app, make an account and come back is three asks too many. So we go where they already are.

**The one idea to protect:** *watching the show is how you progress in the game.* Every other theater on Roblox is a room with a screen. In ours, attention is the currency. If someone cuts every feature but one, keep this.

**The engagement thesis:** a serialized show is already a slot machine. A cliffhanger is a reel still spinning. We wrap casino-grade psychology around it (unpredictable small wins, anticipation before every reveal, the sound of other people winning, status that grows with loyalty), tuned for **coming back** rather than for never leaving. Full playbook in Section 5.3.

**The goal (confirmed by Amy):** keep people watching inside the game, and keep them coming back for more. The game is the destination, not a funnel to the app.

**What success means:**
1. Minutes of bumpp episodes watched per day inside Roblox
2. Share of new players who watch a full chapter in their first session
3. Players who come back for the next episode, and the next Premiere Night
4. Play days per user (Day 1, Days 2 to 7, Days 8 to 28), the signal Roblox ranks on
5. Robux from Blueberry avatar items sold in the game
6. Organic Recommended For You traffic (meaning Roblox's algorithm likes us)

App installs are not a goal for this game.

---

## 1. Hard platform constraints (these shape everything)

Check every item against current Roblox docs before building on it. Rules change often.

### 1.1 Video
From Roblox's Video Frames docs (updated Oct 2026):
- **Max 5 minutes per video**, .mp4 or .mov, up to 4096×2160, under 3.75 GB.
- **2,000 Robux per upload**, **max 20 uploads a day.** Uploader must be a **13+ ID-verified** account. Beta feature: File > Beta Features > Video Uploads.
- **Only two videos can play at the same time** on a client.
- Videos go through moderation before use. Unknown turnaround. **Upload days ahead of any premiere.**
- No documentation on A/V sync or streaming behavior. **Prototype this first** (Section 10, Phase 0).

What this means for the design:
- The 5-minute cap fits our vertical and chapter formats (90 sec to 4 min). Longer ensemble episodes (12 to 25 min) get split into parts that play back to back. Treat part breaks as act breaks in the edit, not dead air.
- The two-video limit means **one live screen per area.** Every other screen (posters, the lobby wall, the screening-room previews) shows still images or animated image sequences, not video. A lobby full of playing TVs won't work.
- Burn subtitles into every video. Most players are outside the US, and many will have sound off (audience bible 2.4 #9, 9.5).
- Video framing: we need both vertical (phone) and horizontal (theater screen) masters. Decide per show which one plays in-game. Recommendation: horizontal on the big screen, vertical cuts in the "phone booth" mini-theaters.

### 1.2 Gambling rules (the casino *psychology* is in Section 5.3; this is just the legal floor)
Roblox banned **simulated gambling** in 2023: virtual chips, simulated betting, playable casino games, **even when no Robux is involved.** You can *show* a casino (that's part of the Moderate label: "unplayable gambling content"), but you can't make it playable.

What *is* allowed is **paid random items** (spins, eggs, chests, blind boxes) under strict rules:
- Show **every possible outcome and its exact numerical odds** before purchase.
- Anything that boosts odds must be explained before purchase too.
- Use **PolicyService** to block paid random items for ineligible users (blocked regions and ages).
- Items from paid random draws **can't be traded or sold** for Robux or anything of value.
- A spin where you can get *nothing* counts as gambling, not a random item. **Every draw must give something.**

**Our approach:** we keep the dopamine and drop the casino. The theme becomes a **blind box**, which this audience already loves (Labubu and Pop Mart are on the "objects of desire" list in bible 9.1). The fun stays: anticipation, reveal, rarity, collecting sets. The legal and reputational risk goes.

### 1.3 Age access and maturity rating
- **Roblox Kids (5 to 8)** gets Minimal/Mild games. **Roblox Select (9 to 15)** gets games up to Moderate. Both only see games that **pass Roblox's selection process.** 16+ sees everything except Restricted.
- New games first go through a **trial phase open only to age-checked 16+ users.** Engagement from that group moves you toward under-16 eligibility.
- **By default, Kids and Select exclude games centered on social hangouts.** That matters a lot here. A "movie theater hangout" could get classified as a hangout and shut off from everyone under 16.
- Developer eligibility for under-16 reach: ID verification, 2-step verification, active Roblox Plus (or Premium).
- Moderate allows "moderate fear-based content," so our horror shows are fine at Moderate. Nothing above Moderate.

**Build rules:**
1. Rate the game **Moderate or lower.** Fill out the maturity questionnaire honestly.
2. **Design and submit it as a game, not a hangout.** Clear objectives, progression and rounds, with hanging out as a side effect, the way Dress to Impress works. **Watching is the round, not a break from it.** See 3.1 for how a showing works as a round. (How Roblox classifies a given game is Roblox's call and isn't fully documented. This is risk management, not a guarantee.)
3. Under-16 reach stays a **decision for Amy** (12.3). Our core audience is 16+, which fits the trial phase. But most of Roblox is under 16.

### 1.4 Selling avatar items inside our own game
Per Roblox's avatar monetization docs, on an **in-experience** sale of an avatar item the **creator gets 30% and the game owner gets 40%.** On a marketplace sale the creator gets 30%.

If Blueberry is both creator and game owner, **we keep about 70% of each in-game sale versus 30% on the marketplace.** This is the strongest financial argument for the game. Confirm Blueberry's actual creator account setup and whether 2D vs 3D items differ (2D publishing changed in July 2026: it now needs ID verification, 2-step verification and Plus/Premium).

APIs to use: `MarketplaceService:PromptPurchase`, the Avatar Inspect Menu, AvatarEditorService for try-on and save. Roblox's **UGC Homestore** template is a good starting point for the shop.

### 1.5 What Roblox's algorithm rewards
From Roblox's Discovery docs (the 28-day model announced June 2026). Signals by priority:

**Most important**
- **Play-through rate:** how many people who see our tile actually play
- **First-play bounce rate** (bad): people leaving in under 60 sec, or in 61 to 180 sec
- **Play days per user:** Day 1, Days 2 to 7, Days 8 to 28
- **Playtime per user**, capped at **60 min per user per game per day**

**Important**
- **Intentional co-play days:** returning to play *with friends* (joins, invites, private servers)
- Qualified play sessions, spend days per user, Robux spent per user

Also: **a custom thumbnail is required** to get any homepage recommendations.

What this means:
- **The first 60 seconds decide whether we get distributed at all.** Someone who spawns into a lobby, sees a long walk and a "next showing in 12:00" sign is gone. The hook has to work instantly (Section 3).
- **Watching together beats watching alone** for the algorithm. Group viewing has to be easier than solo viewing.
- Playtime is capped at 60 minutes a day, so **pushing for 3-hour sessions doesn't help.** Daily return is what counts. Build the economy around coming back tomorrow and next week.

### 1.6 Roblox Moments (Roblox's own short-video feed)
Roblox's in-app feed of 30-second gameplay clips (13+), now in the main app nav. **One tap from a clip drops the viewer into the game.** Our audience bible (A1.8) says Moments is adding direct avatar-item purchases from videos. Verify that.

**This is our free acquisition channel.** Every big moment in the game (the reveal, the runway, the scene recreation) should be built to be recorded and shared to Moments. See the Scene Stage in 4.6.

---

## 2. Who this is for

Full detail is in the **bumpp Audience Intelligence Bible**. What the game design needs from it:

- **Core:** 16 to 19, strongly female, mobile. She may *watch* more than she plays now (girls' gaming drops after 14). Never make her claim a gamer identity.
- **Spillover:** 13 to 15 will come anyway, and possibly under-13s. **Never build anything we wouldn't want a 13-year-old to see.** That's the ceiling.
- **Five cohorts and what each one wants from the park:**
  - **Lore Keepers:** theory boards, rewatch, cast relationships, clue hunts
  - **Drama Girls:** ships, the outfit, the "who will choose whom" vote, glow-up runway
  - **Scream Team:** horror screenings with friends, shared scares, a park area that changes after each episode
  - **The Lobby:** competitive minigames, the leaderboard, team challenges, jokes
  - **Crossover (18 to 24):** prestige look, nostalgia, low lore barrier
- **What wins:** friendship as much as romance, hope over bleakness, fashion as plot, getting chosen.
- **What loses:** cringe, kids'-app visuals, cheap ReelShort energy, dated slang.

**Brand tension to solve (Amy and Ali together):** Roblox hits look loud and memey (Steal a Brainrot is literally built to look like a meme). bumpp's brand is "A24 meets K-drama": understated, lowercase, atmospheric. **Proposal:** a two-layer look. The **park** is bright, glossy and joyful, in the visual language of the shows' worlds (old-money academy, LED midnight rooms, K-pop stage). The **theaters** are dark, cinematic and quiet. Loud outside, prestige inside, like a real cinema lobby versus the auditorium.

---

## 3. The first 60 seconds (the hook)

Goal: someone who taps our tile **feels a reward within 10 seconds** and is **watching a story within 60.**

| Time | What happens | Why |
|---|---|---|
| 0 to 5 s | Spawn straight into the **Premiere Plaza**, not a menu. A huge screen above you is already playing the **cold open of the most dramatic episode** (silent, subtitled, looping the best 20 seconds). | Bible: Episode 1 gets 3x to 7x the views of later episodes. The cold open is our best asset. Lead with it. |
| 5 to 10 s | **Boopp** (our companion character) pops in: "free blind box for your first visit." Tap, it opens with the full reveal animation, and you get a **cast collectible + a wearable item.** | Instant dopamine, something to show off right away, teaches the core collectible. |
| 10 to 30 s | A glowing path leads to the nearest **screening room starting in under 30 seconds.** Rooms open on a short rolling cycle, so there's always one about to start. Friends who join get pulled into the same room. | No waiting. Rolling starts kill "next showing in 12:00." |
| 30 to 60 s | You're in a seat. Chapter 1 of a show starts (90 sec to 4 min). A **Popcorn counter** ticks up while you watch. The room's **Gasp Meter** reacts live. | Watching is progressing, from the very first minute. |
| End of chapter | Payout screen: Popcorn earned, **a Scene Card** from that episode, and a **choice**: "watch part 2 now" (one tap, seat stays) or "go shop her look / play the trivia round." | Bible: end on a decision. Give two ways to keep going, never a dead end. |

Tutorial rule: **no text walls.** Teach by doing. Everything a new player needs is on screen as one glowing button.

### 3.1 How you watch a show when the game has goals and rounds

Watching doesn't sit outside the game loop. **The showing is the round.** It works the way a Dress to Impress round has a dressing phase and then a runway: we have a pre-show, a feature and a post-show. The goals stay light during the episode, so they sharpen your attention without pulling you away from the story.

**A showing = one round (roughly 5 to 10 minutes total)**

| Phase | Length | What you do | Goals in play |
|---|---|---|---|
| **Pre-show** | ~60 to 90 sec | Pick your seat. Grab concessions (cosmetic snacks you hold or throw). Lock in a **prediction** for this episode ("does she open the letter?"). See your **ticket objectives** for the showing. | Make a prediction. Bring a friend (a co-watch bonus). |
| **Feature** | the episode: 90 sec to 5 min per part | Watch. Tap **Golden Popcorn** when it pops (random moments, see 5.3). React with the radial menu at big beats, and the **Gasp Meter** shows whether the room felt it together. **Pause-and-shop** tags save looks to your Wishlist without stopping the show. | Ticket objectives, for example: "catch 3 golden kernels," "react within 2 seconds of the reveal," "spot her signature jacket." Every objective is **passive-friendly**: catching the story pays more than chasing taps. |
| **Post-show** | ~60 to 120 sec | Payout screen. Your prediction resolves. Quick **trivia** (3 to 5 questions on what just happened). Your **Scene Card** reveal. Then a choice: next part, the Wardrobe, or the Runway in tonight's looks. | Score your round. Fill your season track. Keep your streak. |

**Why this works for both watching and gameplay**
- **The story stays the point.** Objectives are small, glanceable and optional. No one has to do anything during the episode except watch. Players who just want to watch still earn the completion payout. Players who want more play the objectives.
- **Attention pays.** Trivia and predictions reward people who actually followed the episode, so the game trains people to watch closely instead of tuning out. Lore Keepers live for this.
- **It reads as a game to Roblox.** Every showing has a clear start, objectives, a score and progression, so it's a structured round with a result, not an open hangout.
- **It suits the algorithm.** Rounds end cleanly, which gives natural "one more" decision points (next part?) and clear stopping points ("back Thursday 7pm for part 3").

**Three ways to watch** (all with rounds)
1. **Public showings:** rolling starts, strangers, the full Gasp Meter crowd. The default.
2. **Private screenings:** your friends, your room, you control start and pause. The co-play driver.
3. **Premiere Night:** one big live showing a week, same day and time, with the Premiere Pot, limited drops and sometimes a cast appearance. The appointment.

**Watching alone is fine too.** Players can always watch in their own Screening Room (4.7), with the same objectives and payouts. Solo watchers keep their streak. Group watchers get a co-watch bonus on top.

### 3.2 The long game: what you're working toward

Every Roblox hit gives you a goal you can *see* from minute one and won't finish for weeks. Ours has three layers, always on screen in one progress panel:

1. **Tonight:** this showing's ticket objectives and the Premiere Pot.
2. **This season:** the **Season Collection**, every Scene Card and cast figurine from the current season's shows, shown as a grid with gaps. Gaps make people come back. Completing a show's set unlocks its exclusive wearable.
3. **Forever:** your **Theater Prestige** and Front Row Club tier, visible to everyone.

**Cast collectibles are the brainrot, made ours.** Steal a Brainrot won because its creatures were already playground currency. Our cast figurines should be **chunky, chibi, instantly recognizable and a little funny**: Mara with her stolen jacket, the villain mid-eyeroll. They're the thing kids screenshot, collect and argue about. They're the *only* place the park goes cute-meme. The shows stay prestige.

**Mutations (from Grow a Garden):** any figurine can come in rare variants: **Gold, Neon, Midnight, and Premiere** (Premiere only drops live on Premiere Night). Same character, different rarity. This multiplies the collection without new art for every item, and gives rare pulls a reason to show off.

**Theater Rebirth (from Steal a Brainrot's rebirth loop):** once your theater hits max prestige level, you can **Rebirth**: reset your decor tier for a permanent Popcorn multiplier and an exclusive marquee sign. This gives long-term players a reason to keep going after they've "finished."

**Trading (Phase 2, from Adopt Me):** trading earned figurines is one of the strongest social retention loops on Roblox. Allow it **only for items earned free** (watching, streaks, events). Anything from a Robux box stays untradeable per 1.2. Use the `IsPaidItemTradingAllowed` check from PolicyService. Build a trade window with preset offers, no free text.

**For longer episodes** (over 5 min, split into parts): one round per part, with a short **intermission** between parts (15 to 30 sec: payout of Golden Popcorn caught so far, one quick prediction for the next part, then it continues automatically). Intermissions are act breaks, not menus. Nobody has to click to keep watching.

---

## 4. The park: zones and features

### 4.1 Premiere Plaza (hub)
- Spawn point, the big screen, the **schedule board** (what premieres when, with a countdown to the next weekly event), the daily reward kiosk, the leaderboard wall.
- **Show doors:** each bumpp show gets a branded entrance in its own world's look. Walking through takes you to that show's wing.

### 4.2 Screening rooms (the core)
- **Public rooms:** rolling starts, 6 to 16 seats (Ali to test what feels full on mobile).
- **Private screening rooms:** invite friends only. This is the main co-play driver, because Roblox's algorithm counts intentional co-play.
- **In-seat reactions:** a radial menu of reactions (gasp, scream, cry, "I KNEW IT," throw popcorn). They aggregate into the **Gasp Meter**, which shows the room's emotional peak at key moments. Pre-mark the big beats in each video's timeline, so the room "erupts" together.
- **Prediction prompts** at the end of each episode ("who sent the message?"). Get it right, earn Popcorn when the next episode confirms it.
- **Seat safety:** reactions are preset, not free text. Text chat follows Roblox's own age-checked chat rules. Don't build our own chat.

### 4.3 The Wardrobe (shop the show)
- Every lead character has a **signature look** (bible 9.4: 2 to 3 defining items plus one turning-point transformation look). Each look lives on a mannequin of the character in the Wardrobe.
- **Try on instantly** (AvatarEditorService), then **buy** (PromptPurchase / Inspect Menu).
- **"Pause and shop":** during an episode, a small non-blocking tag appears when a signature item is on screen ("her jacket"). Tapping it saves the item to your **Wishlist** without stopping the show. The Wishlist opens after the episode.
- **Drop timing:** the transformation look goes on sale the moment its episode premieres, as a time-limited drop. That's the "I need it now" moment.
- Watching gives discounts or early access (see Section 5). The show sells the clothes. The clothes are a reason to watch.

### 4.4 Runway (dress like the cast)
- A Dress to Impress-style round: a theme pulled from the current episode ("dress as Mara on the night she found out"), a 3 to 5 minute timer, a runway walk, star voting.
- Players can use items they own plus a free rotating "costume rack" (so there's no paywall to play).
- **Spite-voting fix:** DTI's best-known complaint is people 1-starring everyone. Options: weight votes by how consistent a voter's ratings are, hide your own score until the end, give voters a "best match" bonus for agreeing with the room. Ali picks, then we test.
- The winner's look gets displayed on a plaza screen (image, not video). Screenshot moment.

### 4.5 Trivia and theory (post-show rounds; the live game show is 4.9)
- **Trivia rounds** after each episode: 5 quick questions, timed, team or solo. Lobby cohort loves competition. Lore Keepers prove they were paying attention.
- **Theory Board:** a wall per show where players pin preset theory cards ("X is lying," "Y and Z are related"). The community's top theories show live as a percentage bar. **Preset cards, not free text**, for safety and moderation.
- **Clue hunts (Scream Team):** after a horror episode, the show's wing physically changes (a door that wasn't there, a flickering sign). Finding the change earns a rare Scene Card. This is how the park feels alive between episodes.

### 4.6 Scene Stage (the fan area, and our biggest new idea)
Fan fiction as typed text is a moderation problem and the wrong format for Roblox. Roblox players already *roleplay*. So:
- Pick a scene from an episode. You get the **costumes, the set and the blocking marks.** The **lines appear as prompts** (karaoke-style). Perform it with friends.
- **Record it** with Roblox's capture tools and share to **Moments.** Every recreation is a free ad that drops viewers straight into our game.
- **"Remix" mode:** the same set, but players choose from a few alternate line options. That's fan fiction in a format that's safe and native.
- **Featured performances:** the bumpp team picks the best fan recreations each week and puts them on the plaza screen. That ties into the bible's participation layer (open auditions drew 770K views).
- **Safety:** preset lines only, no free-text scripts. No private 1:1 spaces between strangers. Report button on every stage. See bible 12.5 on grooming risk in RP communities. This is a real and documented risk in this genre.

### 4.7 Your Screening Room (the base you own)
The proven retention engine on Roblox right now is **owning a place that grows while you're away** (Grow a Garden's idle loop, Steal a Brainrot's base that earns passive income).
- Every player gets a **personal theater.** Decorate it with posters, Scene Cards, cast figurines and seats.
- **Idle earnings:** your theater "screens" episodes you've unlocked and earns Popcorn while you're offline, capped per day so you have to come back. Collect when you return.
- Your theater's **prestige level** shows on your profile and in the plaza (more fans, better premieres).
- Friends can visit and watch in your room. That's another co-play surface.
- **Optional, test carefully:** a light competitive layer, like "steal the spotlight" (a timed mini-challenge to win another player's front-row seat for a premiere). Steal a Brainrot shows that a little rivalry drives huge engagement. We should only add it if it stays playful and doesn't turn into harassment of girls in the core cohort.

### 4.9 bumpp LIVE: our HQ Trivia (the appointment game)

**What HQ got right.** Scheduled live games created a shared cultural moment, with FOMO from the fixed times. Players had 10 seconds to answer, and a wrong answer knocked them out. Referral codes gave out extra lives when friends signed up, and a live viewer count built momentum. A charismatic host (Scott Rogowsky) was the secret ingredient. It went from 3,500 concurrent players in Oct 2017 to 2.38M by March 2018.

**What killed it** (so we design around it):
- **The format stopped changing.** Beyond guest hosts and buying a second chance, HQ ceased to evolve.
- **Tiny shared prizes felt like nothing.** Marketing pushed big jackpots, but the small split wins left players unsatisfied.
- **The host was the product.** When he left, the emotional core left too.
- **Tech:** lag and dropouts kicked players out without warning.
- **Cash prizes were unsustainable.** The company ran out of money.

**Our version: bumpp LIVE, the game show that opens Premiere Night.**

**Format (about 10 to 12 minutes, live, same time every week):**
1. **Doors open (5 min before):** the plaza fills, a countdown runs, and a live player count climbs on the big screen. The count is the hype.
2. **12 questions, 10 seconds each, elimination.** Questions get harder as you go:
   - Q1 to Q4: last week's episode (rewards watchers, easy wins)
   - Q5 to Q8: the season, the cast, the looks ("which jacket did she steal back?")
   - Q9 to Q11: deep lore and theory, plus pop culture that fits the shows
   - **Q12, the final: a question about tonight's episode that hasn't aired yet.** It's a prediction ("does Mara open the letter?"). The answer is revealed *inside the premiere* that follows. Survivors watch the episode to find out if they won. That turns the finale of the game into the cold open of the show.
3. **The Premiere plays** straight after, for everyone who was in LIVE.

**Eliminated players never leave.** Under HQ's format, getting knocked out was a reason to close the app. In ours, eliminated players:
- Stay and play **"Call It"**: they pick what percentage of survivors will get the next question right. Close guesses earn Popcorn.
- Root for a friend still in. You can **"back" a surviving friend**, and if they win, you get a share of the reward.
- Still get the premiere, the Premiere Pot and every live drop.

**Extra lives (the HQ growth loop, kept free):**
- **Encores:** an extra life used automatically on a wrong answer, max **one per game**.
- Earned by: inviting a friend who joins and plays LIVE (the HQ referral loop, which also feeds Roblox's co-play signal), a 7-day watch streak, Front Row Club tier, and finishing last week's episode.
- **Not sold for Robux.** Selling lives in a contest with prizes turns it into pay-to-win, and this audience will call it out. Sell cosmetics around LIVE instead: podium emotes, a winner's spotlight effect.

**The prize (fixing HQ's tiny-split problem):**
- **No cash, no Robux prizes.** Rewards are in-game only.
- **Every winner gets the full prize, not a split.** The reward is a **LIVE Winner exclusive**: a wearable or Premiere-mutation figurine that only that week's winners have, dated ("LIVE winner, wk 3"). Being one of few is the prize, so a small number of winners makes it *more* valuable, not less.
- On top of that, a **Popcorn pot split among winners**, so the split still exists for flavor, but nobody's whole reward hinges on it.
- Winners stand on the **Winner's Podium** during the premiere, visible to everyone in the plaza. Being seen is the reward on Roblox (Dress to Impress proved it).
- Everyone who answers Q1 gets a participation drop, so no one leaves empty-handed.

**The host (and not depending on one person):**
- **Boopp hosts by default.** He's our character, so he can't leave or ask for more money.
- **Special editions:** a cast member (the player behind the avatar) co-hosts on big weeks, like season finales. Per the bible, fans follow the cast as much as the characters.
- **The questions carry the personality**, written in the bible's voice, not stiff quiz copy.

**Keeping it fresh (HQ's fatal flaw):**
- **Rotating formats**, one twist per week: "Lie Detector" (spot the fake quote), "Whose Look?" (name the character from an outfit silhouette), "Order It" (put the scenes in order), "Speed Round" (5 sec answers), "Team LIVE" (your friend group plays as one).
- **A seasonal leaderboard** of LIVE wins and deepest runs, which resets every season.

**More than one slot:** HQ ran on US time. Our audience is mostly outside the US, so run **two LIVE slots a week**, one for US evenings and one for Europe/APAC evenings, each followed by a premiere showing.

**Daily mini-LIVE:** a short 5-question version runs a few times a day on a schedule, with no exclusive prize, just Popcorn and streak credit. This keeps the habit going between weekly shows, the way HQ's daily games did.

**Tech notes for Ali:**
- Roblox runs many separate servers, but LIVE has to feel like **one global game**. Use **MessagingService** to broadcast question start times to every server, and **MemoryStoreService** for the global player count, survivors and the leaderboard. Check current limits on both before designing the broadcast cadence (the docs page I checked didn't list them).
- **Server-authoritative timing:** the server decides when each question opens and closes, with a small latency buffer so mobile players aren't eliminated by lag. HQ's biggest player complaint was getting knocked out by lag.
- If a player disconnects mid-game, let them rejoin into the same game state if they reconnect within ~30 seconds.
- **Load test** before the first live game. Premiere Night spikes are the whole point, and the record Roblox weekends in this audit came with crashes.
- **Question pipeline:** AI drafts the 12 questions from each episode's script and the season bible, then a human reviews every question for accuracy and spoilers. A wrong answer key in front of a live audience is a trust-killer.

### 4.10 Blind Box Booth (the compliant dopamine machine)
- Blind boxes contain **cast collectibles** (figurines for your theater), Scene Cards, emotes and occasional wearables.
- Earned free through watching, daily streaks and events. Also buyable with Robux.
- **If Robux can buy them at all, directly or through a currency bought with Robux,** apply every rule in 1.2: show all outcomes and odds on the box, run PolicyService checks, make paid-random results non-tradeable, and make sure every box gives something.
- Sets: complete a show's full cast set for a rare "premiere badge" and a theater upgrade.
- **Ali, please build the odds display as a shared component** that every random-reward surface has to use, so we can't ship one without it.

---

## 5. Economy

### 5.1 Currencies
| Currency | How you get it | What it's for |
|---|---|---|
| **Popcorn** (soft) | Watching episodes (per minute, with a completion bonus), idle theater earnings, trivia, predictions, runway wins | Free blind boxes, theater decor, costume rack items, seat upgrades |
| **Tickets** (premium) | Robux, plus small free amounts from milestones and events | Premium blind boxes, early access to drops, season pass |
| **Scene Cards** (collectible) | Finishing episodes, clue hunts, live premiere attendance | Sets, profile flex, theater display |

**Anti-farming:** Popcorn from watching only counts when the client is focused and the video is actually playing. Diminishing returns on rewatching the same episode in a day. Capped per day.

### 5.2 Monetization (all Roblox-native)
1. **Avatar items in the Wardrobe** (our 70% take as creator + owner, see 1.4). Biggest line.
2. **Season pass** ("Season Ticket"): a free track plus a paid track tied to each season of shows. Deterministic rewards, no randomness, so no paid-random rules apply.
3. **Game passes:** VIP lounge seat, private screening room upgrades, 2x idle Popcorn, extra Wishlist slots.
4. **Developer products:** Ticket bundles, a one-time "unlock this episode early" (only if early access is a real thing for the show).
5. **Paid blind boxes** under full disclosure rules (1.2).
6. **Rewarded video ads** (Roblox's ad format): optional "watch an ad, get a free box." Brookhaven and Grow a Garden use them. Ads only show to eligible users.
7. **Brand partnerships later:** sponsored screening rooms, branded runway themes. Roblox has said it plans to take a share of in-game brand deal revenue starting 2027. Factor that into pricing.

**Pricing principle:** the free path has to feel generous. This audience shouts about pay-to-win, and the algorithm rewards daily return more than whale spend.

### 5.3 The casino playbook, translated

**Thesis.** A casino doesn't keep people with the jackpot. It keeps them with **anticipation**: the reel spinning, the card about to flip, the sound of someone else winning across the room, small wins arriving often and at unpredictable moments, and the feeling that the place knows who you are. Psychology calls the core engine a **variable-ratio reward schedule**. Rewards that come unpredictably keep people engaged far longer than rewards on a fixed schedule. (That's established behavioral science, not something I re-verified for this doc.)

**Our insight: a serialized show is already a slot machine.** A cliffhanger is a reel still spinning. "Who sent the message?" is the card about to turn. So the game doesn't need to bolt a casino on top. It wraps casino-grade anticipation, feedback and status around the anticipation the story already creates.

**The one adjustment that matters most.** A casino optimizes **session length**, keeping you on the floor as long as possible. Roblox's algorithm caps credited playtime at **60 minutes per user per day** and puts heavy weight on **play days** (Day 1, Days 2 to 7, Days 8 to 28). Hours of bingeing buy us nothing. Coming back tomorrow and next week buys us everything. So every mechanic below is tuned for **return**, not for "never leave."

#### The mechanics

| # | Casino mechanic | Why it works | How we use it |
|---|---|---|---|
| 1 | **Unpredictable small wins** (slot payout schedule) | Not knowing *when* the next reward lands keeps attention high | **Golden Popcorn:** while you watch, golden kernels pop out of the screen at random moments. Tap to grab bonus Popcorn or a surprise Scene Card. Average every 60 to 90 seconds, never on a fixed beat. Watching stays a little alert, never passive. |
| 2 | **The reel spin** (dopamine peaks before the result, not at it) | Anticipation is the high | Every reveal gets a 2 to 3 second build: the blind box shakes, the color of its glow hints at the tier (white, blue, purple, gold), *then* it opens. Same with Scene Cards, trivia results and runway scores. Never instant. Never long enough to annoy. |
| 3 | **The sound of someone else winning** (the floor's noise is the ad) | Seeing others win makes winning feel close | **Server-wide moments:** "lena just pulled the secret Mara figurine" with a chime and a short glow in the plaza. Rare pulls get displayed on the plaza wall for an hour. The Gasp Meter does the same thing for the story: you hear the room react. |
| 4 | **Celebration on every win** (lights, sound, coins clattering) | Makes even small wins feel big and memorable | A sound-and-light language for rewards, scaled by size: a soft pop for Popcorn, confetti for a rare card, a full-screen moment for a set completion. Ali + creative: design this as one system, not one-offs. |
| 5 | **House money** (free play credits) | People spend free credits freely, then they're invested | First-visit blind box, a daily free premium box, small free Ticket gifts at milestones so everyone tries the premium side before paying. |
| 6 | **Comps and the players' club** (tiered status, a card that lights up) | Status and recognition keep people loyal more than prizes | **Front Row Club:** tiers (Usher, Regular, Front Row, Premiere Box) **earned by attendance**: watch days, premieres attended, streaks. Each tier has visible flair (seat color, name glow, a lobby entrance) and real perks (early seats at premieres, first look at drops). **Status comes from showing up, not from spending.** See the "don't" list. |
| 7 | **The high-limit room you can see from the floor** | Visible aspiration | The **Premiere Box balcony** overlooks the main theater and the plaza. Everyone can see who's up there. You get in through Front Row Club tier, not by paying. |
| 8 | **The host who knows your name** | Being recognized feels like belonging | Boopp greets you by name, remembers your show ("mara's back tonight. saved your seat."), and marks your anniversaries in the game (first premiere, 30 days). The bible says the deepest payoff for this audience is **being chosen.** This is that, in a small way. |
| 9 | **Progressive jackpot** (the shared pool that keeps growing) | A visible, rising number everyone's chasing together | **Premiere Pot:** on Premiere Night, a meter fills as the whole server watches. Thresholds unlock drops **for everyone present** (a limited emote at 25%, a wearable at 100%). Cooperative, social, rewards showing up live, and it fills the co-play signal Roblox ranks on. |
| 10 | **Hot streaks** | Momentum feels good, and breaking it feels bad | **Watch streak multiplier** on Popcorn (1x, 1.5x, 2x). Paired with a **free streak freeze** each week so one missed day doesn't wipe it. Loss aversion keeps them coming, and the grace day keeps it from feeling punishing. |
| 11 | **Limited tables and timed promotions** | Scarcity plus a clock creates urgency | Premiere-only drops, transformation looks on sale for 48 hours after their episode, weekly rotating costume rack. (The Admin Abuse model in Section 6.) |
| 12 | **Routing** (the path to the exit runs past the machines) | The next temptation is always in view | Every theater exits through the Wardrobe, where the cast mannequins wear the looks from the episode you just watched. The "next part" button is the biggest thing on the payout screen. **But we don't hide the exit or the clock** (see below). |
| 13 | **Rituals and a sense of control** (blowing on dice, picking "your" machine) | Agency makes chance feel personal | You pick which box off the shelf, you shake it, you choose the seat. In free draws, let players feel ownership of the moment. Prediction prompts and trivia add **real** skill alongside the luck. |
| 14 | **Comp the comeback** (casinos win back lapsed players with offers) | A personal invite back works | Returning after 7+ days triggers a "welcome back" box and a catch-up: "here's what you missed" plays the previous episode's best 30 seconds. Deliver it through Roblox's own notification tools (check current rules for experience notifications). |
| 15 | **Overflow you lose if you don't come back** (expiring free play) | Gives a reason to return on a schedule | Idle Popcorn in your theater fills up to a cap. Past the cap, it stops. Come back to collect. No loss of anything you already earned. |

#### Where we draw the line
The audience includes 13 to 15 year olds and probably younger kids, and everything below gets looked at in Series A diligence, by parents, press and regulators. Some casino techniques work *because* they exploit people. We don't use those:

- **No faked near-misses on random draws.** No showing the legendary "just missing" when the outcome was decided in advance. Near-miss feedback is fine on **skill** outcomes (runway: "2nd by 0.1 stars"; trivia: "one away from the leaderboard").
- **No losses disguised as wins.** Casinos celebrate payouts smaller than the bet. We never celebrate a paid draw that returned less than what was spent as if it were a win.
- **No spend-based VIP status.** Status comes from attendance (mechanic 6). Spending can buy items, never rank over other players.
- **No pressure timers on Robux purchases.** Limited drops are fine. A "buy in the next 30 seconds" countdown on a purchase prompt isn't.
- **No "one more pull" chase prompts** after a bad paid draw.
- **No hidden time.** Unlike a casino, we show natural stopping points ("that's tonight's episode. back Thursday 7pm."). This costs us nothing in ranking (playtime credit caps at 60 min a day anyway) and it's the right thing to do with a teen audience.
- **Any pity timer** (a guaranteed rare after X draws) **on a paid box gets disclosed** with the odds.
- **Variable rewards stay mostly in the free loop.** Golden Popcorn, free boxes and Scene Cards. Paid randomness is a small slice under the full rules in 1.2.

Regulators have already gone after dark patterns in games aimed at young players. The FTC's 2022 settlement with Epic over Fortnite's purchase design is the best-known case. (From my knowledge, not re-verified for this doc.) Staying on the right side of these lines protects the game, the Blueberry brand and the raise.

#### The test for any new mechanic
1. Does it make people want to come **back**, or just make it hard to **leave**? We only want the first.
2. Would we be comfortable explaining it to a parent, and to a journalist?
3. Does the free player still feel lucky?

---

## 6. Retention loops

**Session loop (minutes):** watch a chapter, then get Popcorn and a Scene Card, then make a choice (next part / shop / trivia / runway), then spend on a box or decor, then watch the next chapter.

**Daily loop:** login streak (escalating rewards, a forgiving one-day grace), idle Popcorn to collect, daily trivia, one daily "free premium box."

**Weekly loop (the most important one):**
- **bumpp LIVE opens Premiere Night** (4.9): the HQ-style trivia game show, whose final question gets answered inside the premiere.
- **Premiere Night:** a fixed day and time every week (same slot, never moving, per bible 10.2). New episode, live in-game, with limited drops for people who are there live.
- This is our version of **Admin Abuse.** Grow a Garden and Steal a Brainrot both run scheduled weekly admin events with limited drops, and those events pushed both games past 20M concurrent players. Steal a Brainrot runs them twice a week at fixed times.
- **Mid-week event:** a second, smaller slot (cast Q&A in-game, a runway tournament, a clue hunt drop).
- Every premiere is also a **real update** to the park: new show wing, new looks, new boxes. Steal a Brainrot ships a major update every weekend. Plan for a weekly update cadence from launch.

**Seasonal loop:** a season of shows maps to a season pass, a park theme and a final "finale weekend" event.

**Social loop:** invite rewards (both players get a box), private screening rooms, theater visits, team trivia.

---

## 7. Content plan inside the game

- **Episode format in-game:** 90 sec to 4 min chapters (Drama Girls / Crossover), up to 5 min per part for longer shows. Always burned-in subs.
- **Release cadence:** same time every week. Build a buffer of moderated, uploaded episodes **at least 2 weeks ahead.**
- **Back catalog:** every bumpp show (we have 20+ serialized shows) gets a wing or a shelf. Day-one content is our edge. Most games launch with nothing to watch. We launch with a library.
- **Show-to-game hooks** (writers' room + Ali): each episode ships with its signature look, 5 trivia questions, 1 prediction prompt, 1 Scene Stage scene, and, for horror shows, 1 park change. Make this a required checklist per episode.
- **IP:** use **sets we own** (built in Studio), not third-party maps like Berry Avenue (bible 12.4). That goes for the shows we play and for the park itself.

---

## 8. Look and feel

- **Park:** glossy and bright in the shows' own visual languages: old-money academy, Y2K, coquette, dark academia, K-pop stage, LED midnight rooms with rain on the windows and lavender haze (bible 9.3).
- **Theaters:** dark, cinematic, velvet seats, lit only by the screen. Quiet UI.
- **Faces:** dynamic heads and facial animation on all cast mannequins and NPCs. The bible says this audience treats facial emotion as a production standard.
- **UI copy:** lowercase, short, understated. Never "hey besties," never "slay." Gamer language only in micro-copy (bible 2.6). All UI copy goes through the bible's authenticity QA (8.16).
- **Not:** kids'-app visuals, ReelShort-style composites, cluttered casino neon.
- **Mobile first.** Most Roblox play is on phones. Big tap targets, readable subs on a 6-inch screen, and test on low-end Android, since video plus a detailed world is heavy.

---

## 9. What the market teaches (audit)

| Game | Why it works | What we take |
|---|---|---|
| **Grow a Garden** | Idle farming: plant, leave, come back to growth. Made by a 16-year-old in days. Peaked around 22M concurrent players (a Guinness record). Weekly admin events. | Idle earnings in your own theater. A simple core you understand in 10 seconds. Scheduled weekly events. |
| **Steal a Brainrot** | Built on a meme kids already shared. The loop is buy, earn passive income, steal or get stolen from. Every visual made to be screen-recorded for TikTok. Hit ~25M concurrent in Jan 2026. Twice-weekly fixed admin events, weekly updates. | Make the moments built for recording (Scene Stage, reveals, Gasp Meter). Fixed weekly rhythm. A light, playful rivalry, if it stays kind. |
| **Dress to Impress** | Five-minute dress-up timer, then the whole server watches a runway and votes. Made by a teen (Gigi), pulled in people who don't usually play Roblox, and broke out when big streamers played it. Biggest complaint: spite-voting. | Runway rounds in the cast's looks. Being publicly seen is the reward. Fix the voting. Build for streamers. |
| **Brookhaven RP** | Total freedom to roleplay life. Most-visited game on Roblox ever, still #1 in concurrent players in 2026. | Players will make their own fun if we give them sets and costumes. That's the Scene Stage. |
| **Adopt Me!** | Pet collecting, seasonal egg releases, themed events, years of live ops. | Collect-the-set blind boxes, seasonal drops. |
| **Branded theaters (Regal Jan 2026, Beetlejuice/Fandango, movie premieres)** | Brand activations, mostly short-lived. Regal's theater is an endless runner through a lobby. Warner Bros. sold real tickets in-game. | **Warning:** no Roblox theater has become a lasting hit on its own. A screen in a room isn't a game. Our edge has to be the progression loop and weekly content, not the venue. |

**Patterns across the hits:**
1. You understand the core loop in under 10 seconds.
2. You own something that grows.
3. Collection with visible rarity.
4. Fixed weekly live events plus weekly updates.
5. Built to be screen-recorded and shared.
6. Social stakes: being seen, voted on, stolen from, beaten.
7. Several of them were made by teens, fast, then scaled by a studio. Speed and taste beat polish at launch.

**What's new about us (the experiments):**
1. **Watching is progression.** No top game uses serialized story as its main progression system.
2. **The show sells the outfit live.** Pause-and-shop, plus drops timed to the premiere.
3. **Scene Stage:** fan recreation and remix as play, shared straight to Moments.
4. **Live audience reactions** (Gasp Meter) that make watching together the best way to watch.
5. **The park changes with the story** (clue hunts, horror wings that shift after each episode).
6. **Live cast appearances:** the players behind the avatars show up in-game at premieres. Per the bible, fans follow the cast as much as the characters.
7. **Room votes on branching endings** (later phase): pre-shoot two endings for a few episodes and let a private room's vote decide which one plays. Expensive, so pilot it on one show.

---

## 10. Build phases

No dates here. Ali to estimate after Phase 0.

**Phase 0: kill the technical risks (prototype, ~1 to 2 weeks)**
- Video playback on low-end mobile: frame rate, memory, load time.
- **Sync for group viewing:** server-authoritative start time; clients set `TimePosition` from a shared clock. Measure drift.
- Behavior when a player joins mid-episode, drops out, rejoins.
- The two-simultaneous-video limit in a real layout.
- Moderation turnaround on our first test uploads.
- Confirm the Blueberry creator/owner account setup for the 70% in-game avatar take.
- **Go/no-go:** if group sync or mobile playback doesn't hold up, we rethink before building the park.

**Phase 1: MVP (soft launch to 16+ trial)**
Designer's rule: **launch one tight loop, then add a zone a week.** The hits launched small and grew through weekly updates. Each new zone after launch *is* the weekly update.
- Premiere Plaza with the cold-open screen, the Boopp first-visit box, rolling public screening rooms, private rooms.
- The full showing round (3.1): pre-show prediction, Golden Popcorn, reactions, post-show payout and trivia.
- Popcorn + Scene Cards + cast figurines with mutations, payout screen, "next part" button, the progress panel (3.2).
- Codes, badges, like/favorite prompt, group reward.
- Wardrobe with 2 shows' signature looks, try-on and buy.
- Blind Box Booth with the shared odds component (free boxes only at first is fine).
- Your Screening Room, basic version, with idle Popcorn.
- 2 to 3 shows' back catalogs loaded.
- Analytics events (Section 11), custom thumbnail and icon, maturity questionnaire done.

**Phase 2: live ops**
- Premiere Night weekly event with the Premiere Pot, schedule board, limited drops.
- **bumpp LIVE** (4.9): weekly HQ-style show in two time slots, plus the daily mini-LIVE. Prototype the cross-server sync in Phase 0 alongside video sync.
- Front Row Club tiers, Premiere Box balcony, streak multiplier.
- Runway, Theory Board.
- Season pass, game passes, paid boxes (with full compliance).
- Trading of free-earned figurines, Theater Rebirth.
- Weekly update pipeline.

**Phase 3: the new stuff**
- Scene Stage + Moments sharing, featured fan performances.
- Park changes for horror shows, clue hunts.
- Live cast appearances.
- Branching-ending pilot.

---

## 11. Launch and the basics we have to get right

**Discovery (we need these before any paid push):**
- Custom thumbnail (required for homepage recs) and several thumbnail variants to A/B test. Show a face with an emotion, a second character reacting, and one object hinting at the twist (bible 10.3).
- Title and description written for Roblox search plus trope words ("drama," "romance," "horror").
- First-60-second flow tested on fresh accounts until bounce is low.

**Paid and earned acquisition (this is also where the YouTube/TikTok plan lives):**
- **TikTok and YouTube Shorts clips** from the shows, with every clip pointing to the game. The bible (A1.8) says Roblox Web Play lets a link open the game in a browser. Verify that before relying on it. If it works, it's the cleanest path from a clip to watching inside Roblox.
- **Roblox Sponsored Ads** (Ads Manager) at launch and around each Premiere Night.
- **Roblox YouTubers and streamers:** DTI broke out through streamers. Seed early access and a creator code system.
- **Moments:** the Scene Stage and reveal moments feed this for free.
- **Cast as marketing:** cast Q&As, auditions, "sip or spill" content run *inside* the game as events.

**Roblox table stakes (every hit has these; don't launch without them):**
- **Codes:** a redeem-code box. Drop a new code with every episode, TikTok clip and YouTube upload ("code in the description"). This is the standard Roblox way to turn off-platform viewers into return visits, and it ties our socials to the game.
- **Like + Favorite prompt** after a great moment (a rare pull, a finished episode), never on spawn. Plus a small reward for joining the bumpp Roblox **Community** (group).
- **Badges** for milestones (first premiere, first set, 7-day streak). Players collect them across games.
- **Experience notifications** for Premiere Night and new episodes (check current rules and opt-in limits).
- **Server size and matchmaking** tuned so public showings always have people in them. An empty theater kills the vibe faster than anything.
- **Update log + countdown** on the plaza board. Players come back for the countdown.
- **Leaderboards** (weekly, resetting) for trivia, runway and streaks, so new players can win something this week.
- **Fast loads:** stream in the world, load the plaza first. Mobile players bounce on long loads.

**Community:**
- Discord with the safety rules from bible 12.5: no 1:1 DMs between adult staff and minors, parental consent for minor talent, moderated and logged channels, a reporting path.

**Compliance checklist before launch:**
- [ ] Maturity questionnaire complete, label Moderate or lower
- [ ] Submitted as a game, not a hangout (1.3)
- [ ] Odds shown on every random-reward surface; PolicyService gating; paid-random items non-tradeable; no "win nothing" outcomes
- [ ] No playable gambling of any kind
- [ ] Developer account: ID verified, 2-step verification, Roblox Plus/Premium
- [ ] Video uploader account is 13+ ID verified; every video has the rights cleared; no unlicensed music
- [ ] All sets owned; no third-party maps
- [ ] No free-text UGC surfaces; preset text only
- [ ] Off-platform links (to the bumpp app, socials) follow current Roblox rules. Social links are already hidden from under-16 users as of June 30, 2026. **Ali: check what in-experience linking is allowed now.**

**Analytics (instrument from day one, in Roblox Creator Analytics + custom events):**
Funnel: join, first box opened, first room entered, first chapter started, first chapter finished, second chapter started, Wardrobe visit, try-on, purchase, return D1, return for next Premiere Night.

**Proposed starting targets** (our own guesses, *not* industry benchmarks; replace them with real numbers after two weeks of soft launch):
| Metric | Starting target |
|---|---|
| Leave in under 60 sec | under 30% of new players |
| New players who finish a chapter in session 1 | 50%+ |
| Players who start a 2nd chapter after the 1st | 40%+ |
| Return on Day 1 | 25%+ |
| Back for the next Premiere Night | 20%+ of last week's players |
| Wardrobe visitors who try something on | 30%+ |

**Staffing model: lean, AI-assisted, with named owners.**
The weekly work is mostly content: uploading new episodes, adding each show's looks, trivia, predictions and Scene Cards. AI can do a lot of it: drafting each episode's trivia, predictions and ticket objectives from the script, generating config, writing and refactoring Luau. **Build the game to be data-driven** so a new episode is a content entry (video IDs, looks, questions, objectives, drop dates), not new code. Then the weekly update is mostly an upload.

Four things AI doesn't take off our plate, each needing one named person:
1. **Video pipeline timing:** 20 uploads a day max, moderation turnaround unknown. Someone owns keeping a 2-week buffer of approved episodes.
2. **Live releases:** any code change that touches purchases, player data (DataStores) or the economy gets tested on a staging place before it goes live. A bad update that wipes inventories or breaks a purchase prompt is the fastest way to lose this audience and get review-bombed. AI-written code gets the same review.
3. **Safety and community:** someone human handles reports, the Discord, the Scene Stage and anything involving minors (bible 12.5). Not delegable to a bot.
4. **Premiere Night:** someone is online for the weekly live event, watching server health and ready to roll back.

These can be part-time roles. What matters is that each one has a name.

---

## 12. Open decisions for Amy

1. ~~Funnel or destination?~~ **Decided:** the game is the destination. Success means watching in the game and coming back for more.
2. **Name** of the game.
3. **Under-16 reach:** build to pass the under-16 selection (more players, stricter design and moderation, mostly younger kids) or accept 16+ only (matches the bible's target, smaller pool)?
4. **Light rivalry** (4.7): in or out?
5. **Launch shows:** which 2 to 3 shows open the park. **Suggestion:** one Drama Girls romance (fashion-heavy, which feeds the Wardrobe) and one Scream Team horror (shared scares, park changes).
6. **Owner** for weekly live ops (Section 11).

---

## 13. Sources

Roblox platform:
- Video frames (limits, cost, 2-video cap): https://create.roblox.com/docs/ui/video-frames
- Paid random items policy: https://create.roblox.com/docs/production/monetization/paid-random-items
- Simulated gambling ban context: https://devforum.roblox.com/t/the-definition-of-gambling-on-roblox/1287336/5 and https://devforum.roblox.com/t/is-gambling-allowed-in-specific-content-ratings/3550066
- Content maturity labels: https://create.roblox.com/docs/en-us/production/promotion/content-maturity
- Roblox Kids and Select (publishing requirements): https://create.roblox.com/docs/en-us/production/publishing/kids-and-select
- Kids and Select launch details: https://about.roblox.com/newsroom/2026/04/introducing-roblox-kids-and-select-accounts
- Social links hidden for under-16: https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717
- Discovery signals: https://create.roblox.com/docs/discovery and https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox
- Avatar item payouts: https://create.roblox.com/docs/monetize-avatar
- 2D item changes, July 2026: https://tech-insider.org/roblox-2d-creator-revenue-share-cut-2026/
- Moments: https://about.roblox.com/newsroom/2026/07/moments-new-homepage-unlocks-gaming-for-all

Market:
- Admin Abuse events and the 47M platform record: https://www.tubefilter.com/?p=188004
- Steal a Brainrot event schedule: https://designbeep.com/2026/09/05/when-is-the-next-admin-abuse-in-steal-a-brainrot/
- Steal a Brainrot meme/TikTok design: https://rolearn.dev/case-studies/brainrot-game-meme-culture-25m-ccu
- Grow a Garden analysis: https://rolearn.dev/insights/grow-a-garden-ccu-record-analysis
- Dress to Impress: https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits
- Top games 2026: https://earnaldo.com/blog/best-roblox-games-2026
- Regal theater on Roblox: https://www.fantasylandnews.com/2026/01/15/super-league-regal-open-virtual-movie-theater-on-roblox-for-national-popcorn-day/
- Rewarded video in top games: https://www.glossy.co/?p=196800
- In-game brand deal revenue share from 2027: https://marketingdive.com/news/warner-bros-stirs-up-the-cat-in-the-hat-mayhem-on-roblox-ahead-of-film/833689

Internal:
- bumpp Audience Intelligence Bible (Nov 21, 2026)
