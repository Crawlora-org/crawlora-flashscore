# Crawlora Flashscore Ruby client

This gem calls the Crawlora hosted API at `https://api.crawlora.net/api/v1`. It does not call or scrape Flashscore directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-flashscore"
```

Create an account at [crawlora.net](https://crawlora.net/signup), open the [Crawlora console](https://crawlora.net/app) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/flashscore"

client = Crawlora::Flashscore::Client.new
result = client.request("flashscore-search", JSON.parse("{\"q\": \"football\"}"))
puts result
client.close
```

Use a generated operation method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem contains 38 operations and follows contract revision `sha256:fcaf7e58d82dcbe73e54cddcffc79511b5d01e2c25d511531656862dfe91fb3e`.

```ruby
client = Crawlora::Flashscore::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<contract parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON transport. The gem follows contract revision `sha256:fcaf7e58d82dcbe73e54cddcffc79511b5d01e2c25d511531656862dfe91fb3e` and contains 38 operations.

See [Crawlora](https://crawlora.net/), the [API documentation](https://crawlora.net/docs), and [the package repository](https://github.com/Crawlora-org/crawlora-flashscore) for account setup, the generated operation reference, and release history.
