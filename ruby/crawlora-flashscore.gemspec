require_relative "lib/crawlora/flashscore/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-flashscore"
  spec.version = Crawlora::Flashscore::VERSION
  spec.summary = "Flashscore API client for Crawlora (54 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Flashscore API. Covers scores, match details, competitions, teams, players, odds, and news across 54 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-flashscore", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-flashscore/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
