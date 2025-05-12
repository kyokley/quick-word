{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env = {
    GREET = "quick-work";
    PYTHONPATH = ".";
  };

  # https://devenv.sh/packages/
  packages = [];

  # https://devenv.sh/languages/
  languages = {
    python = {
      enable = true;
      version = "3.12";
      venv.enable = true;
      uv.enable = true;
    };
  };

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
  scripts = {
    hello.exec = ''
      echo Welcome to  $GREET
    '';
    build.exec = ''
      docker build -t kyokley/quick-word .
    '';
    build-dev.exec = ''
      docker build -t kyokley/quick-word --target=dev .
    '';
    shell.exec = ''
      build-dev
      docker run --rm -it --entrypoint bash kyokley/quick-word
    '';
    publish.exec = ''
      build
      docker push kyokley/quick-word
    '';
    tests.exec = ''
      build-dev
      docker run --rm -t --entrypoint uv -v $(pwd):/code kyokley/quick-word run pytest
    '';
  };

  enterShell = ''
    hello
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    tests
  '';

  # https://devenv.sh/git-hooks/
  git-hooks.hooks = {
    ruff.enable = true;
    ruff-format.enable = true;
  };

  # See full reference at https://devenv.sh/reference/options/
}
