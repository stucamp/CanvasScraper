with import <nixpkgs> {}; {
  resumeEnv = stdenv.mkDerivation {
    name = "python38";
    buildInputs = [ 
      stdenv 
      python38Full 
      python38Packages.virtualenv 
    ];

    shellHook = ''
      if [ ! -d venv ]; then
        virtualenv --python=python3.8 venv
        if [ -e requirements.txt ]; then
          ./venv/bin/pip install -r requirements.txt
        fi
      fi
    '';
  };
}
