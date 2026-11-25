#!/usr/bin/env python3
"""Write the entry for make.fun's "The Excuse That Almost Works" bounty.

The entry is the one line a gamer texts the boss to skip work during
GTA 6 launch week. The judge is a tired manager who has heard every
excuse twice and believes almost none of them, so the line has to be:

- one line of plain text, at most 20 words (gate: 1-140 characters);
- believable: a real, specific, boring domestic detail, not a wild story;
- funny on its own terms, the laugh coming from the detail itself;
- written like a text sent in a hurry: no setup, no explanation,
  no signature;
- a fresh angle: no dead grandmother, flat tyre or sudden fever.

The chosen excuse is a burst kitchen pipe. It is mundane and specific
("ankle-deep"), it genuinely takes a day to deal with so a manager can
hardly argue, the vivid detail carries the humour, and it reads exactly
like a 7am text fired off while standing in water.

The joke is the detail, not a punchline: "ankle-deep" turns a boring
plumbing failure into a picture the manager can see, and a flooded flat
is one of the few domestic disasters that plausibly eats a whole workday
— no negotiation, no half-day compromise. The excuse deliberately never
mentions GTA 6: the launch-week occasion is the framing the competition
supplies, not something a real text would advertise, and naming the game
would be the tell that gives the game away to a manager who has heard
every excuse twice. The line wins by being the most believable boring
emergency on the day the gamer most wants to be anywhere but the office.
"""

import os

ENTRY = (
    "Sorry boss, my kitchen pipe burst overnight and the flat's "
    "ankle-deep, waiting on the emergency plumber now."
)


def main() -> None:
    words = ENTRY.split()
    assert len(words) <= 20, f"entry is {len(words)} words, over the 20-word cap"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, outside the 1-140 gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
