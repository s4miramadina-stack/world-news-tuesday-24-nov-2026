# Tuesday 24 November 2026: the world in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/s4miramadina-stack/world-news-tuesday-24-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/s4miramadina-stack/world-news-tuesday-24-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A dense 1024 x 1024 front page for Tuesday 24 November 2026: 30 stories from 7 regions,
four lead cards, a numbered pin map, an hour-by-hour UTC timeline, a "by the numbers"
strip, a certainty label and source on every story, and a DATE CHECK box naming the
true-but-earlier stories that were kept off the page.

- `stories.py` holds every story, its label, source and map position.
- `draw.py` paints the page with Pillow at 2x and writes `entry.png`.
- `main.ts` copies `entry.png` into `$MAKEFUN_OUTPUT_DIR` (default `/output`).

```
python3 draw.py
MAKEFUN_OUTPUT_DIR=./out node main.ts
```

Labels: CONFIRMED (several sources or official data), OFFICIAL (government, agency or
company statement), REPORTED (one wire or outlet), SCHEDULED (set for 24 Nov, result
after the page was made). The map and icons are drawn shapes, not photographs.

MIT licence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1cg5hjc5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
