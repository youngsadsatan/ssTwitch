#!/usr/bin/env python3
import subprocess

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
    # 1) Streamlink
    cmd_sl = [
        "streamlink",
        f"https://www.twitch.tv/{channel}",
        "best",
        "--twitch-disable-ads",
        "--stream-url"
    ]
    try:
        result = subprocess.run(cmd_sl, capture_output=True, text=True, timeout=30)
        url = result.stdout.strip()
        if result.returncode == 0 and url:
            return url
    except Exception:
        pass

    # 2) yt-dlp fallback
    cmd_yd = ["yt-dlp", "--no-check-certificate", "-g", f"https://www.twitch.tv/{channel}"]
    try:
        out = subprocess.check_output(cmd_yd, stderr=subprocess.DEVNULL, timeout=30)
        return out.decode().strip()
    except Exception:
        return None

def main():
    m3u_lines = ["#EXTM3U"]
    for name in sorted(STREAMERS):
        url = get_stream_url(name)
        if url:
            m3u_lines.append(f"#EXTINF:-1,{name}")
            m3u_lines.append(url)
        else:
            print(f"[Aviso] Não foi possível obter stream para {name}. Pode estar offline.")
    # Grava arquivo
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(m3u_lines) + "\n")
    print("✅ playlist.m3u gerada com sucesso.")

if __name__ == "__main__":
    main()
