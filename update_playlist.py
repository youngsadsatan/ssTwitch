#!/usr/bin/env python3
import subprocess
from datetime import datetime

# Streamers List
STREAMERS = [
    "alanzoka",
    "austinshow",
    "bonnie",
    "cinna",
    "emiru",
    "extraemily",
    "familiadapesada_tv",
    "gaules",
    "hasanabi",
    "ijenz",
    "ijenzVOD",
    "juliakins",
    "kaicenat",
    "leanbeefpatty",
    "maya",
    "mira004",
    "mizkif",
    "morgpie",
    "pinkchyu",
    "pokimane",
    "qtcinderella",
    "sakurashymko",
    "sofiaespanha",
    "themajorityreport",
    "tinakitten",
    "tioorochitwitch",
    "uma_pesada_familia_tv",
    "valkyrae",
    "willneff",
]

# Maping the URLs Logos to Streamers channel (tvg-logo)
LOGOS = {
    "alanzoka": "https://static-cdn.jtvnw.net/jtv_user_pictures/64d44235-1dee-4bca-95da-bee1ee96eea3-profile_image-150x150.png",
    "austinshow": "https://static-cdn.jtvnw.net/jtv_user_pictures/9e894c05-6131-4414-bf01-a65e9f88b13a-profile_image-150x150.png",
    "bonnie": "https://static-cdn.jtvnw.net/jtv_user_pictures/11e54a1b-a08e-4bf8-9169-a4470c3e545c-profile_image-150x150.png",
    "cinna": "https://static-cdn.jtvnw.net/jtv_user_pictures/f4e390c8-8f48-4081-b605-475b344fd3aa-profile_image-150x150.png",
    "emiru": "https://static-cdn.jtvnw.net/jtv_user_pictures/c9f74581-c0e8-4638-8629-51dbfe401335-profile_image-150x150.png",
    "extraemily": "https://static-cdn.jtvnw.net/jtv_user_pictures/4d2f4f20-4dba-4866-8a41-542378cb7089-profile_image-150x150.png",
    "familiadapesada_tv": "https://static-cdn.jtvnw.net/jtv_user_pictures/44d9c9a5-3386-4cfc-9c2d-cc47612e4f38-profile_image-150x150.png",
    "gaules": "https://static-cdn.jtvnw.net/jtv_user_pictures/ea0fe422-84bd-4aee-9d10-fd4b0b3a7054-profile_image-150x150.png",
    "hasanabi": "https://static-cdn.jtvnw.net/jtv_user_pictures/0347a9aa-e396-49a5-b0f1-31261704bab8-profile_image-150x150.jpeg",
    "ijenz": "https://static-cdn.jtvnw.net/jtv_user_pictures/45fcecd7-6af2-4f8b-99db-088ba8ae41c0-profile_image-150x150.png",
    "ijenzVOD": "https://static-cdn.jtvnw.net/jtv_user_pictures/f5a54cba-06eb-4353-ad9e-0f4cd4395ae8-profile_image-150x150.png",
    "juliakins": "https://static-cdn.jtvnw.net/jtv_user_pictures/f3d130ae-c5f4-48eb-9a7b-bb09af0ccd6c-profile_image-150x150.png",
    "kaicenat": "https://static-cdn.jtvnw.net/jtv_user_pictures/bf6a04cf-3f44-4986-8eed-5c36bfad542b-profile_image-150x150.png",
    "leanbeefpatty": "https://static-cdn.jtvnw.net/jtv_user_pictures/bea90797-d488-484a-bfa3-4a65e7060f89-profile_image-150x150.png",
    "maya": "https://static-cdn.jtvnw.net/jtv_user_pictures/42b93509-a232-452f-ae01-2051ad6ab1fc-profile_image-150x150.png",
    "mira004": "https://static-cdn.jtvnw.net/jtv_user_pictures/05b52b38-9ddf-4d79-a48c-adc4b262bf13-profile_image-150x150.png",
    "mizkif": "https://static-cdn.jtvnw.net/jtv_user_pictures/ddd88d33-6c4f-424f-9246-5f4978c93148-profile_image-150x150.png",
    "morgpie": "https://static-cdn.jtvnw.net/jtv_user_pictures/ade21f51-8837-47bb-93f5-66971cedf64f-profile_image-150x150.png",
    "pinkchyu": "https://static-cdn.jtvnw.net/jtv_user_pictures/e896554d-b5ed-459d-ab5f-056a7f9d39a3-profile_image-150x150.png",
    "pokimane": "https://static-cdn.jtvnw.net/jtv_user_pictures/912232e8-9e53-4fb7-aac4-14aed07869ca-profile_image-150x150.png",
    "qtcinderella": "https://static-cdn.jtvnw.net/jtv_user_pictures/051f2eb6-fac4-4921-bf65-b87f2177939c-profile_image-150x150.png",
    "sakurashymko": "https://static-cdn.jtvnw.net/jtv_user_pictures/4f49024a-2ad9-4de9-be80-ab31c94f29e7-profile_image-150x150.png",
    "sofiaespanha": "https://static-cdn.jtvnw.net/jtv_user_pictures/c6eb5fa7-8c07-4daf-8101-fa9aa9320abf-profile_image-150x150.png",
    "themajorityreport": "https://static-cdn.jtvnw.net/jtv_user_pictures/e2e7c912-49bf-4df3-bbe4-8ca66d6e8b95-profile_image-150x150.png",
    "tinakitten": "https://static-cdn.jtvnw.net/jtv_user_pictures/4eadab7a-eb89-4205-b89f-6da0b2c2bf36-profile_image-150x150.png",
    "tioorochitwitch": "https://static-cdn.jtvnw.net/jtv_user_pictures/b99a08d2-29ab-4ff1-99eb-01246d41efb7-profile_image-150x150.png",
    "uma_pesada_familia_tv": "https://static-cdn.jtvnw.net/jtv_user_pictures/1b7ac349-8de5-4536-90ee-03451205e3f8-profile_image-150x150.png",
    "valkyrae": "https://static-cdn.jtvnw.net/jtv_user_pictures/a1507999-a5ea-4dd1-911c-63fc493894e6-profile_image-150x150.png",
    "willneff": "https://static-cdn.jtvnw.net/jtv_user_pictures/0526935c-5783-4590-8dc1-16445842633d-profile_image-150x150.png",
}

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
        res = subprocess.run(cmd_sl, capture_output=True, text=True, timeout=60)
        candidate = res.stdout.strip()
        if res.returncode == 0 and candidate:
            print(f"[{channel}] ✅ Streamlink OK")
            return candidate
    except Exception as e:
        print(f"[{channel}] ❌ Streamlink Failed: {e}")

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
            print(f"[{channel}] ✅ yt-dlp OK")
            return url
    except Exception as e:
        print(f"[{channel}] ❌ yt-dlp Failed: {e}")

    return None

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"#EXTM3U", f"# Gerado em {now}"]

    for channel in sorted(STREAMERS, key=str.lower):
        url = get_stream_url(channel)
        if url:
            logo = LOGOS.get(channel)
            if logo:
                lines.append(f'#EXTINF:-1 tvg-logo="{logo}",{channel}')
            else:
                lines.append(f"#EXTINF:-1,{channel}")
            lines.append(url)
        else:
            print(f"[{channel}] ⚠️ Offline or Unavailable")

    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("✅ playlist.m3u atualizada.")

if __name__ == "__main__":
    main()
