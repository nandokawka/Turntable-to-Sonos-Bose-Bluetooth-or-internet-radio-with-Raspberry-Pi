# Turntable to Smart Home Audio (Sonos, Bose) or internet radio with Raspberry Pi

Create a internet radio stream that allows for streaming your records to your Sonos
or any other internet radio endpoint like e.g. the TuneIn App on your
smartphone.

![architecture](./docs/diagrams/setup_of_turntable_to_sonos_or_web_radio_with_raspberry_pi.png
"Architecture")

## TLDR

1. Set audio device to be streamed in `config/darkice.cfg` file.

   ```cfg
   ...
   device          = plughw:3,0 # Audio device for the audio input
   ...
   ```

   See XXX for details about determining your audio device.

2. Start docker container.

   ```bash
   sudo docker compose run --entrypoint "aplay -l" record-stream
   ```

The numbering of the audio devices is not deterministic and changes randomly
after a restart.

[[_TOC_]]

## Setup and configuration

### Concept

The audio hardware in the households changes drastically and makes use of
technologies like bluetooth or wireless streaming. This goes along with the
removal of physical connectors on the audio devices. As a consequence it becomes
harder if not impossible at the first glimpse to listen to your records on playback devices in your household. This project tackles this problem with the
help of a docker container that creates a live internet radio stream in the
local network from the current playing record. This internet radio stream can be consumed by any internet radio compatible device in the
network. E.g. you can add the created internet radio stream to your smart home
audio system from [Sonos](https://www.sonos.com/de-de/home) or [Bose Home Audio](https://www.bose.com/en_us/products/speakers/smart_home.html) as well as any other bluetooth sound system or computer.

### Architecture

The pipeline begins with the record player which is connected to the USB audio
interface (see architecture overview above). The analog signal from the current playing record travels through USB
audio interface into the Raspberry PI. The program
[Darkice](http://www.darkice.org/) encodes the analog audio signal into a
digital audio signal according to your configuration and sends it to a streaming
media server. The streaming media server in this setup is
[Icecast](https://icecast.org/). It creates a internet radio station in your
private network. You can listen to it on any device that allows for the
connection with an internet radio stream.
To create a similar set you need to complete the following steps.

1. Organize Hardware.
2. Prepare Raspberry PI.
3. Make number of used audio interface persistent.
4. Install required software.
5. Configure Darkice.

### Hardware

1. Record player with stereo out.
2. USB Audio interface with phono preamp e.g.:
   1. [Behringer U-PHONE
      UFO202](https://www.amazon.de/-/en/gp/product/B002GHBYZ0/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) (tested).
   2. If your record player has a build in phono preamp or you are using an
      external phono you can also use audio boards from
      [HifiBerry](https://www.hifiberry.com/shop/#boards) (not tested).
3. Raspberry PI e.g.:
   1. Raspberry PI 4 2GB Ram (tested).
   2. Other versions should also work.
4. Audio System eg.:
   1. [Sonos](https://www.sonos.com/de-de/home) including [Sonos
      App](https://apps.apple.com/de/app/sonos/id1488977981?l=en) (tested).
   2. Any Bluetooth speaker plus internet radio app e.g.
      [TuneIn](https://tunein.com/) (tested) or similar.
   3. [Bose Home Audio](https://www.bose.com/en_us/products/speakers/smart_home.html) (not
      tested) including [Bose Music
      APP](https://www.bose.de/de_de/apps/bose_music.html) (not tested).

####

#####


### Persistent audio device number

As alsa is indexing the available audio devices randomly on every reboot. In order to configure the record streamer correctly we need to make the assigned number of our audio interface persistent. This can be done in various ways as described [here](https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture#top-page) for arch linux. The following command lists the loaded audio kernel modules.

```bash
lsmod | grep snd
```

With this information you can configure the card index in a persistent way by adding the file `/etc/modprobe.d/alsa-base.conf` and set the index of your desired module e.g.:

```bash
options snd_usb_audio index=3
```

[*Add an Internet radio station to
Sonos*](https://support.sonos.com/en/article/add-an-internet-radio-station-to-sonos)

## Thanks to

### Icons used

<a href="https://www.flaticon.com/de/kostenlose-icons/vinyl" title="vinyl Icons">Vinyl Icons erstellt von Pavel Kozlov - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/speaker" title="speaker icons">Speaker icons created by Smashicons - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/raspberry-pi" title="raspberry pi icons">Raspberry pi icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/laptop" title="laptop icons">Laptop
icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/audio" title="audio icons">Audio icons created by Andrejs Kirma - Flaticon</a>