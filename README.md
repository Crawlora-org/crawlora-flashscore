# Flashscore clients for Crawlora

Official Crawlora client packages for the hosted Flashscore API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape Flashscore locally. Crawlora is an independent service and is not affiliated with or endorsed by Flashscore or its owners.

- JavaScript / TypeScript: [`@crawlora-org/flashscore`](javascript/README.md)
- Python: [`crawlora-flashscore`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-flashscore`](go.mod)
- Ruby: [`crawlora-flashscore`](ruby/README.md)
- Java: [`net.crawlora:crawlora-flashscore:0.3.0`](java/README.md)
- PHP: [`crawlora/flashscore`](php/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)
- Source repository: [https://github.com/Crawlora-org/crawlora-flashscore](https://github.com/Crawlora-org/crawlora-flashscore)

Create an account at [crawlora.net](https://crawlora.net/signup), open the [Crawlora console](https://crawlora.net/app) to get an API key, or read the [API documentation](https://crawlora.net/docs).

## Install

```sh
npm install @crawlora-org/flashscore
python -m pip install crawlora-flashscore
go get github.com/Crawlora-org/crawlora-flashscore@latest
gem install crawlora-flashscore
composer require crawlora/flashscore
```

For Java, add `net.crawlora:crawlora-flashscore:0.3.0` to your Maven dependencies; see [java/README.md](java/README.md).

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## PHP example

The Packagist package is available as `crawlora/flashscore`:

```sh
composer require crawlora/flashscore
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$apiKey = getenv('CRAWLORA_API_KEY');
if (!$apiKey) throw new RuntimeException('Set CRAWLORA_API_KEY before running this example.');
$client = new \Crawlora\Flashscore\Client(apiKey: $apiKey);
$result = $client->request("flashscore-sports", []);
print_r($result);
$client->close();
```

The same example and install details are in [php/README.md](php/README.md).

## License

MIT. See [LICENSE](LICENSE).
