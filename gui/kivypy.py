## Kivy
from forest._importable import LazyImport

kivy = LazyImport("import kivy", "PACKAGE kivy — Open source UI framework written in Python, derived from 'import kivy', from https://github.com/kivy/kivy, Documentation: https://kivy.org/doc/stable/")
kivyApp = LazyImport("from kivy.app import App as kivyApp", "CLASS kivyApp derived from kivy.app.App — Base for creating Kivy applications, derived from 'from kivy.app import App as kivyApp', from https://github.com/kivy/kivy, Documentation: https://kivy.org/doc/stable/api-kivy.app.html")
kivyuilds = LazyImport("import kivy.uix as kivyuilds", "SUBPACKAGE kivyuilds derived from kivy.uix — Classes for creating and managing Widgets, derived from 'import kivy.uix as kivyuilds', from https://github.com/kivy/kivy, Documentation: https://kivy.org/doc/stable/api-kivy.uix.html")
