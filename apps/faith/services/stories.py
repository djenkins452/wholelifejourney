
# apps/faith/services/stories.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class BibleStory:
    slug: str
    title: str
    story: str          # FULL long-form narrative
    why_it_matters: str
    reference_links: List[dict]




def get_stories() -> List[BibleStory]:
    # Phase 1: curated set. No embellishing — but engaging.
    # IMPORTANT: We precompute scripture lookup URLs here to keep templates logic-free.
    def link(label: str, t: str, b: str, c: int, v: str) -> dict:
        return {"label": label, "url": f"/faith/scripture/?t={t}&b={b}&c={c}&v={v}"}

    return [
        BibleStory(
		    slug="creation",
		    title="Creation",
		    story=(
		        "In the beginning, there was nothing but darkness and emptiness. Then God spoke, and light appeared. "
		        "God separated the light from the darkness and named them day and night. This was the first day.\n\n"

		        "On the following days, God created the sky, the land, and the seas. He filled the earth with plants, "
		        "trees, and every kind of vegetation. He placed the sun, moon, and stars in the sky to mark seasons "
		        "and time.\n\n"

		        "God then created animals—fish in the sea, birds in the air, and creatures that walked on land. "
		        "Finally, God created people in His own image. He gave them responsibility to care for the earth "
		        "and all living things.\n\n"

		        "When God finished His work, He rested on the seventh day. He looked at everything He had made "
		        "and declared it very good."
		    ),
		    why_it_matters=(
		        "This story shows that God created everything with purpose and care. It teaches that people are "
		        "valuable because they are made in God’s image and are meant to care for His creation."
		    ),
		    reference_links=[
		        link("Genesis 1–2", "BSB", "GEN", 1, "1-31"),
		    ],
		),

		BibleStory(
		    slug="adam-and-eve",
		    title="Adam and Eve",
		    story=(
		        "God created Adam and Eve and placed them in the beautiful Garden of Eden. The garden had everything "
		        "they needed—food, water, and peace. God walked with them and gave them only one rule: they were not "
		        "to eat from the tree of the knowledge of good and evil.\n\n"

		        "One day, a serpent tricked Eve into doubting God’s command. She ate the fruit and gave some to Adam. "
		        "Immediately, they felt shame and realized they had disobeyed God. They tried to hide when God came "
		        "to find them.\n\n"

		        "God spoke with Adam and Eve about their choice and explained the consequences. Life would now include "
		        "hard work and pain. Even so, God showed mercy by clothing them and caring for them as they left the garden."
		    ),
		    why_it_matters=(
		        "This story explains how sin entered the world and why people struggle to obey God. It also shows that "
		        "God still seeks and cares for people even when they fail."
		    ),
		    reference_links=[
		        link("Genesis 3", "BSB", "GEN", 3, "1-24"),
		    ],
		),

		BibleStory(
		    slug="noahs-ark",
		    title="Noah’s Ark",
		    story=(
		        "The world had become filled with violence and evil, but Noah chose to obey God. God told Noah that "
		        "a great flood was coming and instructed him to build a huge ark.\n\n"

		        "Noah followed God’s instructions carefully. He brought his family and pairs of animals into the ark. "
		        "Soon, rain fell for forty days and nights, covering the earth with water.\n\n"

		        "After many months, the waters slowly dried up. God placed a rainbow in the sky as a promise that "
		        "He would never again destroy the entire earth with a flood."
		    ),
		    why_it_matters=(
		        "This story teaches obedience and trust. It also shows God’s justice, mercy, and faithfulness to His promises."
		    ),
		    reference_links=[
		        link("Genesis 6–9", "BSB", "GEN", 6, "1-22"),
		    ],
		),

		BibleStory(
		    slug="abraham-promise",
		    title="God’s Promise to Abraham",
		    story=(
		        "God called Abraham to leave his home and travel to a land He would show him. Abraham did not know "
		        "where he was going, but he trusted God and obeyed.\n\n"

		        "God promised Abraham that he would become the father of a great nation, even though he and his wife "
		        "Sarah had no children and were very old.\n\n"

		        "Abraham believed God’s promise. God counted Abraham’s faith as righteousness and promised blessings "
		        "for all nations through his family."
		    ),
		    why_it_matters=(
		        "This story teaches that faith means trusting God’s promises, even when they seem impossible."
		    ),
		    reference_links=[
		        link("Genesis 12; 15", "BSB", "GEN", 12, "1-9"),
		    ],
		),

		BibleStory(
		    slug="joseph",
		    title="Joseph and His Brothers",
		    story=(
		        "Joseph was loved deeply by his father, which made his brothers jealous. They sold him into slavery "
		        "and told their father that Joseph was dead.\n\n"

		        "Joseph was taken to Egypt, where he faced many hardships. Even when treated unfairly, he trusted God. "
		        "God helped Joseph rise to a position of great authority.\n\n"

		        "When famine struck the land, Joseph’s brothers came to Egypt for help. Joseph forgave them and saved "
		        "his family, showing mercy instead of revenge."
		    ),
		    why_it_matters=(
		        "This story shows how God can use painful situations for good and teaches the power of forgiveness."
		    ),
		    reference_links=[
		        link("Genesis 37–50", "BSB", "GEN", 37, "1-36"),
		    ],
		),

		BibleStory(
		    slug="moses-burning-bush",
		    title="Moses and the Burning Bush",
		    story=(
		        "While tending sheep, Moses saw a bush that was on fire but did not burn up. God spoke to Moses from "
		        "the bush and called him by name.\n\n"

		        "God told Moses to return to Egypt and free the Israelites from slavery. Moses felt afraid and made "
		        "excuses, saying he was not a good speaker.\n\n"

		        "God reassured Moses that He would be with him and gave him signs to show His power. Moses finally "
		        "accepted God’s calling."
		    ),
		    why_it_matters=(
		        "This story shows that God can use imperfect people and gives courage to those who feel unqualified."
		    ),
		    reference_links=[
		        link("Exodus 3", "BSB", "EXO", 3, "1-12"),
		    ],
		),

		BibleStory(
		    slug="ten-commandments",
		    title="The Ten Commandments",
		    story=(
		        "After freeing Israel from slavery, God led His people to Mount Sinai. There, God spoke to Moses "
		        "and gave him ten commandments.\n\n"

		        "These laws taught the people how to worship God and how to treat one another with honesty and respect.\n\n"

		        "The commandments helped guide Israel’s daily life and showed them how to live in a way that honored God."
		    ),
		    why_it_matters=(
		        "The Ten Commandments help people understand right and wrong and show God’s desire for justice and love."
		    ),
		    reference_links=[
		        link("Exodus 20", "BSB", "EXO", 20, "1-17"),
		    ],
		),

		BibleStory(
		    slug="joshua-jericho",
		    title="The Fall of Jericho",
		    story=(
		        "God told Joshua to lead Israel against the city of Jericho, whose walls were tall and strong.\n\n"

		        "Instead of attacking, God commanded the people to march around the city once a day for six days. "
		        "On the seventh day, they marched seven times and shouted.\n\n"

		        "The walls of Jericho fell down, and Israel won the battle through obedience to God."
		    ),
		    why_it_matters=(
		        "This story teaches that success comes from trusting and obeying God, not relying on strength alone."
		    ),
		    reference_links=[
		        link("Joshua 6", "BSB", "JOS", 6, "1-27"),
		    ],
		),

		BibleStory(
		    slug="gideon",
		    title="Gideon",
		    story=(
		        "God chose Gideon to rescue Israel from its enemies. Gideon felt weak and unsure of himself.\n\n"

		        "God reduced Gideon’s army so that the victory would clearly come from Him and not human strength.\n\n"

		        "With God’s help, Gideon led Israel to victory, proving that God’s power is greater than fear."
		    ),
		    why_it_matters=(
		        "This story teaches that God’s strength is shown best when people depend on Him."
		    ),
		    reference_links=[
		        link("Judges 6–7", "BSB", "JDG", 6, "1-40"),
		    ],
		),

		BibleStory(
		    slug="ruth",
		    title="Ruth",
		    story=(
		        "Ruth chose to stay with her mother-in-law Naomi after both of their husbands died. She promised "
		        "to follow Naomi and trust Naomi’s God.\n\n"

		        "Ruth worked hard to provide food, gathering grain in the fields. Her kindness and faithfulness "
		        "caught the attention of a man named Boaz.\n\n"

		        "God blessed Ruth by giving her a new family and making her part of the family line of Jesus."
		    ),
		    why_it_matters=(
		        "This story teaches loyalty, kindness, and trusting God during difficult seasons."
		    ),
		    reference_links=[
		        link("Ruth 1–4", "BSB", "RUT", 1, "1-22"),
		    ],
		),
		BibleStory(
		    slug="samuel-calling",
		    title="God Calls Samuel",
		    story=(
		        "Samuel was a young boy who lived and worked in God’s house under the care of Eli the priest. "
		        "One night, while Samuel was sleeping, he heard a voice calling his name.\n\n"

		        "Samuel ran to Eli, thinking he had called him, but Eli said he had not. This happened three times "
		        "before Eli realized it was God speaking to Samuel.\n\n"

		        "Eli told Samuel to listen and respond to God. Samuel obeyed, and God began speaking to him regularly. "
		        "Samuel grew up to be a faithful prophet who guided Israel."
		    ),
		    why_it_matters=(
		        "This story teaches that God speaks to those who are willing to listen and obey, no matter their age."
		    ),
		    reference_links=[
		        link("1 Samuel 3", "BSB", "1SA", 3, "1-21"),
		    ],
		),

		BibleStory(
		    slug="david-goliath",
		    title="David and Goliath",
		    story=(
		        "The Philistine army had a giant warrior named Goliath who mocked Israel and challenged them to fight. "
		        "All of Israel’s soldiers were afraid.\n\n"

		        "David, a young shepherd, came to bring food to his brothers. When he heard Goliath’s insults, David "
		        "trusted that God would help him win.\n\n"

		        "Using only a sling and one stone, David defeated Goliath. God showed that victory comes through faith, "
		        "not size or strength."
		    ),
		    why_it_matters=(
		        "This story teaches courage and reminds us that trusting God is more powerful than fear."
		    ),
		    reference_links=[
		        link("1 Samuel 17", "BSB", "1SA", 17, "1-58"),
		    ],
		),

		BibleStory(
		    slug="solomon-wisdom",
		    title="Solomon Asks for Wisdom",
		    story=(
		        "When Solomon became king, God appeared to him in a dream and offered to give him anything he asked for.\n\n"

		        "Instead of asking for riches or power, Solomon asked for wisdom so he could rule the people fairly.\n\n"

		        "God was pleased and gave Solomon great wisdom, along with wealth and honor. Solomon became known as "
		        "the wisest king in Israel."
		    ),
		    why_it_matters=(
		        "This story teaches that wisdom and good judgment are more valuable than riches."
		    ),
		    reference_links=[
		        link("1 Kings 3", "BSB", "1KI", 3, "1-15"),
		    ],
		),

		BibleStory(
		    slug="elijah-fire",
		    title="Elijah on Mount Carmel",
		    story=(
		        "The people of Israel were worshiping false gods, and Elijah challenged the prophets of Baal to a test.\n\n"

		        "Both sides prepared sacrifices, but only the true God would answer with fire. The false prophets cried "
		        "out all day, but nothing happened.\n\n"

		        "When Elijah prayed, God sent fire from heaven and burned the sacrifice completely. The people knew the "
		        "Lord was the one true God."
		    ),
		    why_it_matters=(
		        "This story shows that God is real, powerful, and worthy of trust and worship."
		    ),
		    reference_links=[
		        link("1 Kings 18", "BSB", "1KI", 18, "16-39"),
		    ],
		),

		BibleStory(
		    slug="jonah",
		    title="Jonah",
		    story=(
		        "God told Jonah to go to the city of Nineveh and warn the people to turn from their evil ways. "
		        "Jonah did not want to go and ran the opposite direction.\n\n"

		        "A storm came, and Jonah was thrown into the sea, where a great fish swallowed him. Inside the fish, "
		        "Jonah prayed and asked God for forgiveness.\n\n"

		        "God gave Jonah another chance. Jonah obeyed, and the people of Nineveh repented. God showed mercy to them."
		    ),
		    why_it_matters=(
		        "This story teaches that God’s mercy is for everyone and that obedience matters."
		    ),
		    reference_links=[
		        link("Jonah 1–4", "BSB", "JON", 1, "1-17"),
		    ],
		),

		BibleStory(
		    slug="daniel-lions",
		    title="Daniel in the Lions’ Den",
		    story=(
		        "Daniel faithfully prayed to God every day, even when it became illegal. His enemies reported him "
		        "to the king.\n\n"

		        "Daniel was thrown into a den of lions, but God sent an angel to shut the lions’ mouths.\n\n"

		        "Daniel was unharmed, and the king praised God, recognizing His power."
		    ),
		    why_it_matters=(
		        "This story teaches faithfulness and trusting God even when obedience is dangerous."
		    ),
		    reference_links=[
		        link("Daniel 6", "BSB", "DAN", 6, "1-28"),
		    ],
		),

		BibleStory(
		    slug="birth-of-jesus",
		    title="The Birth of Jesus",
		    story=(
		        "Jesus was born in the town of Bethlehem to Mary and Joseph. There was no room in the inn, so "
		        "Jesus was placed in a manger.\n\n"

		        "Angels appeared to shepherds nearby and announced the birth of the Savior. The shepherds hurried "
		        "to see the baby.\n\n"

		        "Jesus’ birth fulfilled God’s promise to send a Savior for the world."
		    ),
		    why_it_matters=(
		        "This story shows God’s love by sending Jesus to live among people."
		    ),
		    reference_links=[
		        link("Luke 2:1–20", "BSB", "LUK", 2, "1-20"),
		    ],
		),

		BibleStory(
		    slug="jesus-baptism",
		    title="Jesus Is Baptized",
		    story=(
		        "Jesus came to the Jordan River to be baptized by John. At first, John hesitated, but Jesus insisted.\n\n"

		        "As Jesus came up from the water, the Holy Spirit descended like a dove, and a voice from heaven "
		        "said Jesus was God’s beloved Son.\n\n"

		        "This moment marked the beginning of Jesus’ public ministry."
		    ),
		    why_it_matters=(
		        "This story shows Jesus’ obedience and confirms who He is."
		    ),
		    reference_links=[
		        link("Matthew 3", "BSB", "MAT", 3, "13-17"),
		    ],
		),

		BibleStory(
		    slug="good-samaritan",
		    title="The Good Samaritan",
		    story=(
		        "Jesus told a story about a man who was attacked and left hurt on the road. Several people saw him "
		        "but chose to walk away.\n\n"

		        "A Samaritan stopped to help, bandaging the man’s wounds and paying for his care.\n\n"

		        "Jesus taught that loving others means helping anyone in need, even those who are different from us."
		    ),
		    why_it_matters=(
		        "This story teaches compassion and what it truly means to love your neighbor."
		    ),
		    reference_links=[
		        link("Luke 10:25–37", "BSB", "LUK", 10, "25-37"),
		    ],
		),

		BibleStory(
		    slug="feeding-5000",
		    title="Feeding the 5,000",
		    story=(
		        "A huge crowd followed Jesus to hear Him teach. When they became hungry, there was very little food.\n\n"

		        "A boy shared five loaves of bread and two fish. Jesus thanked God and multiplied the food.\n\n"

		        "Everyone ate until they were full, and leftovers remained."
		    ),
		    why_it_matters=(
		        "This story shows that God can do great things with small acts of faith."
		    ),
		    reference_links=[
		        link("John 6:1–14", "BSB", "JHN", 6, "1-14"),
		    ],
		),

		BibleStory(
		    slug="calming-storm",
		    title="Jesus Calms the Storm",
		    story=(
		        "While crossing the sea, a violent storm frightened the disciples. Waves filled the boat.\n\n"

		        "Jesus spoke and calmed the storm immediately. The wind and waves obeyed Him.\n\n"

		        "The disciples realized Jesus had power over nature."
		    ),
		    why_it_matters=(
		        "This story teaches that Jesus brings peace in the middle of fear."
		    ),
		    reference_links=[
		        link("Mark 4:35–41", "BSB", "MRK", 4, "35-41"),
		    ],
		),

		BibleStory(
		    slug="last-supper",
		    title="The Last Supper",
		    story=(
		        "Jesus shared a final meal with His disciples before His arrest. He broke bread and shared wine.\n\n"

		        "Jesus explained that His body and blood would be given for them.\n\n"

		        "He asked His followers to remember Him through this meal."
		    ),
		    why_it_matters=(
		        "This story reminds believers of Jesus’ sacrifice and love."
		    ),
		    reference_links=[
		        link("Luke 22:14–20", "BSB", "LUK", 22, "14-20"),
		    ],
		),

		BibleStory(
		    slug="crucifixion",
		    title="The Crucifixion",
		    story=(
		        "Jesus was arrested, mocked, and sentenced to die, even though He had done nothing wrong.\n\n"

		        "He was nailed to a cross and prayed for forgiveness for those hurting Him.\n\n"

		        "Jesus gave His life to save others."
		    ),
		    why_it_matters=(
		        "This story shows the depth of God’s love and forgiveness."
		    ),
		    reference_links=[
		        link("Luke 23", "BSB", "LUK", 23, "26-49"),
		    ],
		),

		BibleStory(
		    slug="resurrection",
		    title="The Resurrection",
		    story=(
		        "Three days after Jesus died, women went to His tomb and found it empty.\n\n"

		        "An angel told them Jesus was alive. Jesus later appeared to His followers.\n\n"

		        "Jesus defeated death and gave hope to the world."
		    ),
		    why_it_matters=(
		        "The resurrection brings hope, new life, and victory over death."
		    ),
		    reference_links=[
		        link("Luke 24", "BSB", "LUK", 24, "1-12"),
		    ],
		),

		BibleStory(
		    slug="great-commission",
		    title="The Great Commission",
		    story=(
		        "After rising from the dead, Jesus met His disciples and gave them a mission.\n\n"

		        "He told them to go into the world and teach others about Him.\n\n"

		        "Jesus promised to be with them always."
		    ),
		    why_it_matters=(
		        "This story gives believers purpose and direction."
		    ),
		    reference_links=[
		        link("Matthew 28:16–20", "BSB", "MAT", 28, "16-20"),
		    ],
		),



    ]



def get_not_everyone_knows_guidance() -> List[str]:
    return [
        "Assume good intent: people often say “everyone knows” as shorthand, not as a jab.",
        "Normalize learning: “I’ve heard parts of it—can you walk me through it?” is a strong, humble question.",
        "Ask for the reference: “Where is that in Scripture?” helps the whole group stay grounded.",
        "Invite clarity gently: “Let’s recap the key moment for anyone who’s new to it.”",
        "Leaders set tone: the healthiest groups celebrate questions, not just familiarity.",
    ]
