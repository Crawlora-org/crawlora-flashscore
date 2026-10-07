import { FlashscoreClient } from "@crawlora-org/flashscore";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FlashscoreClient({ apiKey });

  const sports = await client.sports({  });
  console.log("sports", sports);
  const scores = await client.scores({ sport: "football", day_offset: 0 });
  console.log("scores", scores);
