# Flashscore clients for Crawlora

Official Crawlora client packages for the hosted Flashscore API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape Flashscore locally. Crawlora is an independent service and is not affiliated with or endorsed by Flashscore or its owners.

- JavaScript / TypeScript: [`@crawlora-org/flashscore`](javascript/README.md)
- Python: [`crawlora-flashscore`](python/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)
- Source repository: [https://github.com/Crawlora-org/crawlora-flashscore](https://github.com/Crawlora-org/crawlora-flashscore)

## Install

```sh
npm install @crawlora-org/flashscore
python -m pip install crawlora-flashscore
```

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## Contract

This package release is `0.1.0`. The generated client methods follow the bundled `openapi/public.json` contract at revision `sha256:380bb303ffcb6ff808a1db512dcc3bd90c9b7d20d62e64d1b368f37c9a6771bd`. `scripts/generate.py` regenerates both language clients and the documentation from the shared source.

## License

MIT. See [LICENSE](LICENSE).
