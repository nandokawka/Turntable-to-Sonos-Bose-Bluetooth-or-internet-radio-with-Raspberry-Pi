from diagrams import Diagram, Node, Edge, Cluster
from diagrams.custom import Custom

graph_attr = {
  "splines": "curved",
  "layout": "neato",
  "margin":"-2, -2"
}

with Diagram('\nSetup of Turntable to Sonos or Web Radio with Raspberry Pi', show=True, graph_attr=graph_attr) as diag:
  
  with Cluster("Household"):
    Node("", shape="plaintext", pin="true", pos="0.5,0.5")
    Node("", shape="plaintext", pin="true", pos="19.5,5.5")
    record_player = Custom("Record player", "./png/schallplattenspieler.png", pin="true", pos="1,3")
    audio_device = Custom("Audio device", "./png/usb.png", pin="true", pos="5,3")
    audio = Custom("App", "./png/audio.png", pin="true", pos="16,3")
    sonos = Custom("Sonos System", "./png/speaker.png", pin="true", pos="19,5")
    speaker = Custom("BT Speaker", "./png/speaker.png", pin="true", pos="19,3")
    laptop = Custom("Laptop", "./png/laptop.png", pin="true", pos="19,1")

  with Cluster("Raspberry PI", graph_attr={"bgcolor": "thistle"}):
    Node("", shape="plaintext", pin="true", pos="7.4,5")
    Node("", shape="plaintext", pin="true", pos="12.5,1")
    rpi = Custom(
      "", "./png/raspberry-pi.png",
      fontsize="6", loc="t",
      fixedsize="true", width="1", height="1", 
      pin="true", pos="9.8,4.5")
    darkice = Custom("Darkice", "./png/darkice.png", pin="true", pos="8,3")
    icecast = Custom("Icecast", "./png/icecast-bw.png", pin="true", pos="12,3")

  record_player >> Edge(label="analog audio") >> audio_device
  # Edge(headlabel="analog audio signal", labelangle="0", labeldistance="14", constraint="False") >> audio_device
  audio_device >> darkice
  darkice >>  Edge(label="encoded audio") >> icecast
  icecast >> Edge(label="internet\nradio stream") >> audio
  audio >> [sonos, laptop, speaker]
  