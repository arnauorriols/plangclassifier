PLangClassifier
===============
Programming language Classifier. Stripped down fork of https://github.com/douban/linguist. 

All credit goes to https://github.com/douban/linguist. This is just the classifier extracted from that repo. 

Installation
============

pip install -e git+https://github.com/arnauorriols/plangclassifier#egg=plangclassifier

Usage
=====

>>> from plangclassifier import classify_langs
>>>
>>> snippet = """
-define(INFO_KEYS, [name, type, durable, auto_delete, internal, arguments,
                    policy]).

recover() ->
    Xs = rabbit_misc:table_filter(
           fun (#exchange{name = XName}) ->
                   mnesia:read({rabbit_exchange, XName}) =:= []
           end,
           fun (X, Tx) ->
                   X1 = case Tx of
                            true  -> store_ram(X);
                            false -> rabbit_exchange_decorator:set(X)
                        end,
                   callback(X1, create, map_create_tx(Tx), [X1])
           end,
           rabbit_durable_exchange),
    [XName || #exchange{name = XName} <- Xs].
"""
>>> classify_langs(snippet, languages=['Python', 'Erlang', 'JavaScript', 'Haskell'])
[('Erlang', -693.5272278989029), ('JavaScript', -715.8595787671218), ('Prolog', -744.0383123253338), ('Python', -793.2415599562956)]

Languages supported
-------------------

* TypeScript
* edn
* Ceylon
* Rebol
* Shell
* AppleScript
* Arduino
* SuperCollider
* Nginx
* Opa
* Agda
* Logos
* Parrot Assembly
* Sass
* Kotlin
* Standard ML
* Objective-C
* Groovy Server Pages
* Handlebars
* Gosu
* Less
* COBOL
* Visual Basic
* PHP
* Groovy
* Java
* Scala
* ApacheConf
* Makefile
* Perl
* Lua
* Verilog
* Forth
* XProc
* wisp
* Literate CoffeeScript
* RobotFramework
* CoffeeScript
* Awk
* Idris
* Ruby
* LFE
* C
* AutoHotkey
* Scaml
* Logtalk
* Clojure
* Rust
* Prolog
* Jade
* YAML
* INI
* Literate Agda
* Lasso
* GLSL
* ECL
* VHDL
* Elm
* OpenCL
* Nu
* SCSS
* Oxygene
* BlitzBasic
* Turing
* Processing
* Bluespec
* NSIS
* JSON
* NetLogo
* CSS
* Emacs Lisp
* fish
* XML
* XSLT
* XC
* MoonScript
* Nemerle
* Cuda
* KRL
* Scilab
* Markdown
* Tea
* OCaml
* Protocol Buffer
* Volt
* Pascal
* UnrealScript
* Diff
* Ragel in Ruby Host
* Parrot Internal Representation
* DM
* Ioke
* Monkey
* PogoScript
* Apex
* LiveScript
* JavaScript
* VimL
* OpenEdge ABL
* ABAP
* Matlab
* Slash
* Erlang
* Scheme
* Squirrel
* Python
* Max
* GAS
* Common Lisp
* Dart
* XQuery
* Omgrofl
* Nimrod
* Coq
* Xtend
* M
* C++
* TXL
* TeX
* Julia
* R
* Racket
* Haml
* PowerShell

