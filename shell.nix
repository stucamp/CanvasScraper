with import<nixpkgs> {};

stdenv.mkDerivation rec {
name = "env";

  dependencies = [
    python38
    python38Packages.toolz
    python38Packages.selenium
    python38Packages.youtube-dl
  ];

  env = buildEnv {
    name = name;
    paths = dependencies;
  };

}
