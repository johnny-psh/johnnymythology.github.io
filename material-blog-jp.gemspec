# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "material-blog-jp"
  spec.version       = "0.3.0"
  spec.authors       = ["Johnny Pan"]
  spec.email         = ["contact@johnnypan.me"]

  spec.summary       = "Created a theme for my blog using Material Design Lite."
  spec.homepage      = "https://www.johnnypan.me"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }
  
  spec.add_runtime_dependency "jekyll", "~> 3.8"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.6.1"

  spec.add_development_dependency "bundler", ">= 2.2.10"
  spec.add_development_dependency "rake", "~> 12.0"
end
