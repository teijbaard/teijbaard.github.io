source "https://rubygems.org"

gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sitemap"
end

# Ruby 3.4+ compatibility: stdlib gems verplaatst naar bundled gems
gem "csv"
gem "base64"
gem "bigdecimal"

# Windows/JRuby compatibility
platforms :windows, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
