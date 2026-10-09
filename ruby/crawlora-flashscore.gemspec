require_relative "lib/crawlora/flashscore/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-flashscore"
  spec.version = Crawlora::Flashscore::VERSION
  spec.summary = "Flashscore client for the Crawlora hosted API"
  spec.description = "Credential-free Flashscore API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-flashscore", "documentation_uri" => "https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-api-docs", "rubygems_mfa_required" => "true" }

end
