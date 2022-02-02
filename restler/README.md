# RESTler commands

RESTler added using official Microsoft [Repo](https://github.com/microsoft/restler-fuzzer)

## Setting up RESTler
- Din root directory executati in terminal:
  ``docker build -t restler .``
- Creati restler_bin:
 ``mkdir restler_bin``
- Executati din root directory:
 ``py -3.7 ./build-restler.py --dest_dir "######"``
- "###" = "C:...." Directory restler_bin

## Quick Start

- ``py -3.7 restler-quick-start.py --api_spec_path "C:\Users\Sorin\Desktop\ANUL 3\SEM 1\Inginerie Software\3\ProiectIS\APIDocumentation\OpenAPI\openapi.yaml" --restler_drop_dir "C:\Users\Sorin\Desktop\ANUL 3\SEM 1\Inginerie Software\3\ProiectIS\restler_bin"``

- How to run RESTler test:
``.\restler test --grammar_file "C:\Users\Sorin\Desktop\ANUL 3\SEM 1\Inginerie Software\3\ProiectIS\restler_working_dir\Compile\grammar.py" --dictionary_file "C:\Users\Sorin\Desktop\ANUL 3\SEM 1\Inginerie Software\3\ProiectIS\restler_working_dir\Compile\dict.json" --settings "C:\Users\Sorin\Desktop\ANUL 3\SEM 1\Inginerie Software\3\ProiectIS\restler_working_dir\Compile\engine_settings.json" --no_ssl``