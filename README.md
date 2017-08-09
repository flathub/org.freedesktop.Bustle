# Flatpak for [Bustle](https://www.freedesktop.org/wiki/Software/Bustle/)

Someone's favourite D-Bus profiler, now available on someone's favourite app distribution platform.

## Updating the manifest

* `org.freedesktop.Bustle.yaml` is the human-editable master copy of the manifest. It uses JSON-style syntax, plus `#` comments.
* `org.freedesktop.Bustle.json` is the copy that's actually used to build the Flatpak.
* After modifying the YAML version, run `update-manifest.py` to regenerate the JSON version, and commit both.

This slightly unusual setup is to allow comments in the human-editable version of the manifest, without leaning on a json-glib misfeature where `/* c-style comments */` are supported but `/* c-style comments / containing slashes */` are not.
