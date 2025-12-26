<h1 align="center">⚡ X (Twitter) Video Downloader PRO</h1>

<p align="center">
  <b>Fast • GPU Accelerated • Python GUI</b><br>
  Download X (Twitter) videos in seconds with thumbnail preview & HEVC encoding
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/Platform-Windows-green?logo=windows">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>📥 Download X / Twitter videos (.mp4 / .ts / .mov)</li>
  <li>🖼 Live thumbnail preview + auto-save</li>
  <li>📊 Real-time progress bar</li>
  <li>🌙 Dark & Light mode toggle</li>
  <li>📂 Custom download folder</li>
  <li>🎞 Format selector (Best / MP4 / Audio)</li>
  <li>🔥 GPU HEVC encoding (NVIDIA RTX / AMD / CPU fallback)</li>
  <li>🧠 Automatic GPU detection</li>
</ul>

<h2>🧠 GPU Acceleration</h2>

<table>
<tr>
<th>GPU</th>
<th>Encoder</th>
</tr>
<tr>
<td>NVIDIA RTX</td>
<td>hevc_nvenc</td>
</tr>
<tr>
<td>AMD Radeon</td>
<td>hevc_amf</td>
</tr>
<tr>
<td>No GPU</td>
<td>libx265 (CPU)</td>
</tr>
</table>

<h2>🛠 Requirements</h2>

<pre>
Python 3.9+
yt-dlp
ffmpeg (must be in PATH)
</pre>

<h2>📦 Installation</h2>

<pre>
pip install yt-dlp pillow requests
</pre>

<p>
Download FFmpeg:
<a href="https://www.gyan.dev/ffmpeg/builds/" target="_blank">
https://www.gyan.dev/ffmpeg/builds/
</a>
</p>

<h2>▶️ Usage</h2>
<ol>
  <li>Run the Python script</li>
  <li>Paste X (Twitter) video URL</li>
  <li>Choose format & folder</li>
  <li>Click <b>Download</b></li>
</ol>

<h2>📸 Preview</h2>
<p align="center">
  <img src="preview.png" width="700">
</p>

<h2>⚠️ Disclaimer</h2>
<p>
This tool is for <b>educational purposes only</b>.  
Respect X (Twitter) Terms of Service and content creators’ rights.
</p>

<hr>

<p align="center">
⭐ Star this repo if you found it useful!  
</p>
