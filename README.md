# Turntable to Sonos or Webradio with Raspberry Pi

Create a web radio stream that allows for streaming your records to your Sonos or any other web radio stream compatible endpoint in your network.

```bash
sudo docker compose run --entrypoint "aplay -l" record-stream
```

As alsa is indexing the available soundcards randomly on every reboot. In order to confifure the record streamer correctly we need to make the assigned number of our audio interface persistent. This can be done in various ways as described [here](https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture#top-page) for arch linux. The following command lists the loaded audio kernel modules.

```bash
lsmod | grep snd
```

With this information you can configure the card index in a persistent way by adding the file `/etc/modprobe.d/alsa-base.conf` and set the index of your desired module e.g.:

```bash
options snd_usb_audio index=3
```



