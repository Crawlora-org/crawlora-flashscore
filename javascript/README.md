# @crawlora-org/flashscore

JavaScript and TypeScript client for Crawlora's hosted Flashscore API.
It calls [Crawlora](https://crawlora.net); it does not run a browser or scrape Flashscore locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Flashscore or its owners.

## Install

```sh
npm install @crawlora-org/flashscore
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup), then open the [Crawlora console](https://crawlora.net/app) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { FlashscoreClient } from "@crawlora-org/flashscore";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FlashscoreClient({ apiKey });
const result1 = await client.sports({});
console.log(result1);
const result2 = await client.scores({ sport: "football", day_offset: 0 });
console.log(result2);
```

The client also exports `Client` as an alias for `FlashscoreClient`. Operation
methods are available directly in camelCase and through the `flashscore`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/examples/javascript.mjs) for contract-backed examples and text transcript output where supported.

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API; response data and availability follow that
service's current contract.
