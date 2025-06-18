#!/usr/bin/env python3
import subprocess
from datetime import datetime

STREAMERS = [
    "alanzoka",
    "emiru",
    "extraemily",
    "gaules",
    "hasanabi",
    "pokimane",
    "qtcinderella",
    "sofiaespanha",
    "themajorityreport",
    "tioorochitwitch",
    "valkyrae",
    "willneff"
]

def get_stream_url(channel: str) -> str | None:
    """
    Tenta obter a URL HLS via Streamlink (sem anúncios).
    Se falhar, tenta usar yt-dlp como fallback.
    """
    url = None

    # 1) Streamlink
    cmd_sl = [
        "streamlink",
        f"https://www.twitch.tv/{channel}",
        "best",
        "--twitch-disable-ads",
        "--stream-url"
    ]
    try:
        res = subprocess.run(cmd_sl, capture_output=True, text=True, timeout=60)
        candidate = res.stdout.strip()
        if res.returncode == 0 and candidate:
            print(f"[{channel}] ▶️ Streamlink OK")
            return candidate
    except Exception as e:
        print(f"[{channel}] ❌ Streamlink falhou: {e}")

    # 2) yt-dlp fallback
    cmd_yd = [
        "yt-dlp",
        "--no-check-certificate",
        "-g",
        f"https://www.twitch.tv/{channel}"
    ]
    try:
        out = subprocess.check_output(cmd_yd, stderr=subprocess.DEVNULL, timeout=60)
        url = out.decode().strip()
        if url:
            print(f"[{channel}] ▶️ yt-dlp OK")
            return url
    except Exception as e:
        print(f"[{channel}] ❌ yt-dlp falhou: {e}")

    return None

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"#EXTM3U", f"# Gerado em {now}"]
    for channel in sorted(STREAMERS, key=str.lower):
        url = get_stream_url(channel)
        if url:
            lines.append(f"#EXTINF:-1,{channel}")
            lines.append(url)
        else:
            print(f"[{channel}] ⚠️ offline ou indisponível")
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("✅ playlist.m3u atualizada.")

if __name__ == "__main__":
    main()
