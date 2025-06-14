import subprocess

# Lista de streamers do Twitch (nomes de canal)
streamers = [
    "alanzoka", "emiru", "extraemily", "gaules", "hasanabi", 
    "pokimane", "qtcinderella", "sofiaespanha", 
    "themajorityreport", "tioorochitwitch", "valkyrae", "willneff"
]

# Abre o arquivo de saída (M3U) e escreve o cabeçalho
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name in streamers:
        # Comando Streamlink para obter o URL da stream (melhor qualidade, sem anúncios)
        cmd = [
            "streamlink",
            f"https://www.twitch.tv/{name}",
            "best",
            "--twitch-disable-ads",
            "--stream-url"
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            url = result.stdout.strip()
            if result.returncode == 0 and url:
                # Escreve o cabeçalho EXTINF com o nome do canal e o URL do stream
                f.write(f"#EXTINF:-1,{name}\n{url}\n")
            else:
                print(f"[Aviso] Não foi possível obter stream para {name}. Pode estar offline.")
        except Exception as e:
            print(f"[Erro] Streamlink falhou para {name}: {e}")
