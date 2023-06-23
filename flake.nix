{
  description = "verb conjugation";
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-23.05";
    flake-utils.url = github:numtide/flake-utils;
  };
  outputs = { self, nixpkgs, flake-utils }:
    with flake-utils.lib; eachSystem allSystems (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        lttoolbox = pkgs.stdenv.mkDerivation {
          src = pkgs.fetchFromGitHub {
            owner = "apertium";
            repo = "lttoolbox";
            rev = "3d82cd337e81877f20f7ad79ea398ad184fae5ac";
            sha256 = "sha256-3lHXKtwQSrMGQEGOGr27e3kB2qKkTFZcEzeAnIm89Rg=";
          };
          name = "lttoolbox";
          buildInputs = [
            pkgs.autoconf
            pkgs.automake
            pkgs.libtool
            pkgs.libxml2
            pkgs.libxml2.dev
            pkgs.icu
            pkgs.pkg-config
            pkgs.utf8cpp
          ];
          buildFlags = [
            "CPPFLAGS=-I${pkgs.utf8cpp}/include/utf8cpp"
          ];
          configurePhase = ''
            ./autogen.sh --prefix $out
          '';
        };
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
            lttoolbox
          ];
          shellHook = ''
            export PATH=$PATH:./node_modules/.bin/
          '';
        };
      });
}
