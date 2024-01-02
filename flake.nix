{
  description = "verb conjugation";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = github:numtide/flake-utils;
  };
  outputs = { self, nixpkgs, flake-utils }:
    with flake-utils.lib; eachSystem allSystems (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        # defaultPackage = packages.document;
        devShell = pkgs.mkShell {
          # development environment
          buildInputs = [
            pkgs.nodejs-18_x
            pkgs.nodePackages.npm
            pkgs.python3
            pkgs.yq-go
            pkgs.jq
            pkgs.ffmpeg
            pkgs.lttoolbox
          ];
          shellHook = ''
            export PATH=$PATH:./node_modules/.bin/
          '';
        };
      });
}
