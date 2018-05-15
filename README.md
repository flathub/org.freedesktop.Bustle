# Flatpak for [Bustle](https://www.freedesktop.org/wiki/Software/Bustle/)

Someone's favourite D-Bus profiler, now available on someone's favourite app distribution platform. [Install it here](https://flathub.org/apps/details/org.freedesktop.Bustle).

## Building and testing locally

```console
$ rm -rf _build && \
  flatpak-builder --install --user _build org.freedesktop.Bustle.yaml && \
  flatpak run org.freedesktop.Bustle//master
```
