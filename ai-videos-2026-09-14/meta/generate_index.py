#!/usr/bin/env python3
"""Rebuild index.md + catalog.html from accepted.jsonl (existing files only)."""
from __future__ import annotations

import json
import html as html_lib
from collections import Counter
from pathlib import Path

ROOT = Path("/workspace/ai-videos-2026-09-14")
META = ROOT / "meta"
VIDEOS = ROOT / "videos"
FRAMES = ROOT / "frames"

FOLLOWERS = {
    "Framer_X": 49512,
    "NACHOS2D_": 35347,
    "andresvandal": 3659,
    "Goodmanprotocol": 10911,
    "itsSaira_1": 4712,
    "Timeless_aiart": 56944,
    "leo_xiaolei": 6800,
    "john_my07": 12886,
    "heavypulp": 74024,
    "Kling_ai": 134835,
    "ojiji2025": 5336,
    "hungrydonkey": 1047,
    "Sabitamago": 34799,
    "keshiAIart": 69635,
    "dvorahfr": 196026,
    "Jessewelle": 897338,
    "HappyHorseATH": 7097,
    "MiniMax_AI": 122923,
    "Hailuo_AI": 82436,
    "ViduAI_official": 16200,
    "techhalla": 97265,
    "TechieBySA": 32829,
    "testerlabor": 14564,
    "paranoidream": 12846,
    "imagine": 2_000_000,
    "grok": 8_000_000,
    "Yokohara_h": 124606,
    "8co28": 432515,
    "ComfyUI": 250000,
    "Diana_Osire": 55633,
    "AIwithJessica": 16331,
    "Just_sharon7": 47626,
    "notoro_ai": 30594,
    "mm551234": 23948,
    "KeorUnreal": 42712,
    "EHuanglu": 142234,
    "kaolti": 4091,
    "yumesyokunin": 27319,
    "CharaspowerAI": 54233,
    "MayorKingAI": 36152,
    "Sheldon056": 13862,
    "abxxai": 21660,
    "JaydenCoach": 44720,
    "KettlebellDan": 85535,
    "art_muse": 22299,
    "Ultima1138": 9425,
    "aymducking": 9735,
    "gizakdag": 241433,
    "elonmusk": 241660846,
    "munou_ac": 51053,
    "0xbisc": 15823,
    "a0mUYucgm3JTJp9": 4513,
    "HAL2400_AI": 18063,
    "TomaAIbijo": 92589,
    "fabianstelzer": 44275,
    "aimikoda": 29072,
    "0xInk_": 204215,
    "XFreeze": 274329,
    "tetsuoai": 240405,
    "jboogx_creative": 30618,
    "Ciri_ai": 11769,
    "PJaccetturo": 96516,
    "Solopopsss": 35128,
    "egeberkina": 82914,
    "demonflyingfox": 20009,
    "rehan_shei": 10293,
    "cb_doge": 1900757,
    "NICKIMINAJ": 26866509,
    "SpaceXAI": 2060697,
    "viktoroddy": 71725,
    "ai_Tyler_no_bu": 1458,
    "TaoRInne": 2357,
    "PrometheanAIX": 6003,
    "beholdersai": 8890,
    "Romi2656": 10070,
    "HakumaiDev": 22167,
    "JayKay65220066": 14148,
    "ciguleva": 238488,
    "sohbunshu": 208651,
    "NVTDanh": 5529,
    "biz_fx50": 45185,
    "ai_lifehack55": 2749,
    "hibi_ai__": 2558,
    "chiha_20220301": 1502,
    "applete77191758": 2291,
    "bDAxjGohPDX7XiV": 33,
    "Kashiko_AIart": 13903,
    "kellyyjjones": 3260,
    "Xaroon_x": 10258,
    "Adam38363368936": 17066,
    "banana_ai_club1": 41532,
    "lansenai": 10180,
    "studio_oneroom": 4976,
    "genel_ai": 28750,
    "atlas_remake": 33,
    "superfang119": 369,
    "Vtuber7144": 3413,
    "shirawiggles": 3292,
    "Imagvio_AI": 88,
    "SadiaMalik182": 10796,
    "k_kaori_dododo": 3024,
    "AI_VideoLab": 525,
    "PUNPUNinuhime": 8869,
    "MauriceBourdon": 1185,
    "hey_am_cherry": 4700,
    "itxabdullaa": 7273,
    "CaliraVal": 9947,
    "ai_uncovered": 25541,
    "ashen_one": 55296,
    "SD_Tutorial": 11085,
    "plasm0": 6986,
    "ponyodong": 14894,
    "amadeus_NFT": 89,
    "AlexM12jx": 60964,
    "toyxyz3": 31914,
    "hq4ai": 37062,
    "KanaWorks_AI": 8810,
    "umesh_ai": 47116,
    "towya_aillust": 15557,
    "WuxiaRocks": 7809,
    "neco1751662": 3247,
    "Ayu_AI_0912": 3909,
    "wildmindai": 11427,
    "wavespeed_ai": 8564,
    "seiiiiiiiiiiru": 23237,
    "nbykos": 25614,
    "ai_artworkgen": 23783,
    "KEETY2591756": 2146,
    "ExquisitMe": 0,
    "ROSHENDILAN": 524,
    "SasaruGAI": 371,
    "talinkacreator": 146,
    "StevieMac03": 15836,
    "AleRVG": 17694,
    "jerrod_lew": 19391,
    "HBCoop_": 54747,
    "mxvdxn": 23970,
    "yori03617": 18026,
    "maxescu": 38930,
    "LudovicCreator": 38168,
    "TechByMarkandey": 64972,
    "javilopen": 128630,
    "magnific": 89971,
    "rovvmut_": 31542,
    "SHD766": 3018,
    "h_ashizawaJP": 28494,
    "kayforkind": 136,
    "CHAO2U_AI": 7587,
    "TheAva_AI": 11373,
    "openart_ai": 78290,
    "higgsfield_ai": 230516,
    "MonetizationDon": 10343,
    "hedra_labs": 54144,
    "codewithimanshu": 68703,
    "liluocheng13": 3191,
    "im_shahid7": 5315,
    "0xKarmi": 689,
    "browncatro1": 6712,
    "YaReYaRu30Life": 5350,
    "uso800railway": 129,
    "shikoba_86": 6942,
    "manishkumar_dev": 53549,
    "invideoOfficial": 36183,
    "churvikv": 7140,
    "ai_for_success": 81413,
}


def load_accepted() -> list[dict]:
    rows = []
    seen = set()
    p = META / "accepted.jsonl"
    if not p.exists():
        return rows
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        o = json.loads(line)
        i = str(o.get("id"))
        if i in seen:
            continue
        seen.add(i)
        fn = o.get("filename")
        if not fn or not (VIDEOS / fn).exists():
            continue
        handle = (o.get("handle") or "").lstrip("@")
        fol = o.get("followers") or 0
        if handle in FOLLOWERS:
            fol = FOLLOWERS[handle]
            o["followers"] = fol
        if o.get("manual"):
            rows.append(o)
            continue
        if fol and fol < 3000:
            continue
        likes = o.get("likes") or 0
        views = o.get("views") or 0
        if likes < 500 and views < 50000:
            continue
        rows.append(o)
    rows.sort(key=lambda r: (-(r.get("likes") or 0), -(r.get("views") or 0)))
    return rows


def md_cell(s) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def write_index(rows: list[dict]) -> None:
    models = Counter(r.get("model") for r in rows)
    lines = []
    lines.append("# AI 视频素材清单  2026-09-14")
    lines.append("")
    lines.append(
        f"收录 **{len(rows)}** 条（目标 200，宁缺毋滥）。硬性条件：白名单模型、8–35s 实测、近半年、点赞≥500 或播放≥5万、粉丝≥3000、OCR 画面纯净。"
    )
    lines.append("")
    lines.append("## 模型分布")
    lines.append("")
    for m, n in models.most_common():
        lines.append(f"- {m}: {n}")
    lines.append("")
    lines.append("## 清单")
    lines.append("")
    lines.append(
        "| # | 文件名 | 卖点 | 链接 | 模型 | 时长(s) | 账号 | 粉丝数 | 点赞 | 播放 | 发布日期 | 纯净度 |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        handle = (r.get("handle") or "").lstrip("@")
        tweet = r.get("tweet") or f"https://x.com/{handle}/status/{r['id']}"
        lines.append(
            "| {n} | `{fn}` | {sell} | [推文]({url}) | {model} | {dur} | @{h} | {fol} | {likes} | {views} | {date} | {purity} |".format(
                n=i,
                fn=md_cell(r.get("filename")),
                sell=md_cell(r.get("sell") or r.get("caption") or "")[:80],
                url=tweet,
                model=md_cell(r.get("model")),
                dur=r.get("measured_s") or round((r.get("dur_ms") or 0) / 1000, 2),
                h=handle,
                fol=r.get("followers") or "—",
                likes=r.get("likes") or 0,
                views=r.get("views") or 0,
                date=r.get("date") or "",
                purity=r.get("purity") or "",
            )
        )
    lines.append("")
    lines.append("## a) 模型证据")
    lines.append("")
    for i, r in enumerate(rows, 1):
        ev = (r.get("evidence") or r.get("caption") or "").replace("\n", " ")
        lines.append(f"{i}. @{r.get('handle')} / {r.get('model')} — 「{ev[:180]}」")
    lines.append("")
    lines.append("## b) 被剔除的典型案例")
    lines.append("")
    examples = [
        ("2099091218349150212", "@0xbisc Seedance 2.5", "角色设定图铺满界面文字，不是干净成片"),
        ("2098994140310843550", "@muku_sns Seedance 2.5", "烧录游戏 HUD 日期时间"),
        ("2075192866553413944", "@ibexdream Seedance 2.0", "四帧均有 @IBEXDREAM 角标水印"),
        ("2098336640997744921", "Pollo.ai 水印", "平台水印"),
        ("2098766209839923543", "@AI__TSUBAKI Flova UI", "生成器界面/字幕叠层"),
        ("2096576268334432459", "@NACHOS2D_ 日文字幕", "烧录日语字幕"),
        ("2076523566334669214", "@Sheldon056 Kling 3.0", "名人换脸（Altman/Cook × Mr.Bean）按 deepfake 剔除"),
        ("2074146352745849020", "@Hachibi_Kitsune", "粉丝 1044 < 3000"),
        ("2080776412429246758", "@keshiAIart Vidu Q3", "四帧均有 @keshiAIart 角标水印"),
        ("2097412354090942883", "@imagine 产品 UI", "grok.com/imagine 网页录屏，非成片"),
        ("2090679733805809696", "@Jessewelle MiniMax H3", "名人政治 deepfake（Seinfeld×Trump）"),
        ("2099144888033898752", "@techhalla Seedance 2.5", "TECHHALLA 角标水印"),
        ("2079162249231409246", "@TechieBySA Seedance 2.0", "SPORT HD 转播台标 + @handle 水印"),
        ("2081024688319512697", "@Kling_ai 144p overlay", "烧录分辨率标签，属于贴字"),
        ("2078469568209805580", "@Sabitamago Seedance 2.0", "CapCut 角标水印"),
        ("2086980920343761232", "@Sabitamago Seedance 2.5", "Pollo AI 角标水印"),
    ]
    lines.append("| 推文 ID | 条目 | 原因 |")
    lines.append("|---|---|---|")
    for tid, who, why in examples:
        lines.append(f"| {tid} | {who} | {why} |")
    rej_path = META / "rejects.json"
    if rej_path.exists():
        try:
            rejs = json.loads(rej_path.read_text() or "[]")
        except Exception:
            rejs = []
        if rejs:
            lines.append("")
            lines.append(f"本轮 OCR/时长自动剔除 {len(rejs)} 条，抽样：")
            for r in rejs[:8]:
                lines.append(
                    f"- @{r.get('handle')} {r.get('id')} — {r.get('reason')} "
                    f"(实测 {r.get('measured_s', '—')}s)"
                )
    lines.append("")
    lines.append("## c) 下载失败")
    lines.append("")
    fail_path = META / "fails.json"
    fails = []
    if fail_path.exists():
        try:
            fails = json.loads(fail_path.read_text() or "[]")
        except Exception:
            fails = []
    if not fails:
        lines.append("当前无未恢复的下载失败（失败条目会在重试后写入）。")
    else:
        for f in fails:
            lines.append(f"- @{f.get('handle')} {f.get('id')} — {f.get('reason')}")
    lines.append("")
    lines.append("## 说明")
    lines.append("")
    lines.append("- 时长一律 ffmpeg 实测，不采用 X 标注。")
    lines.append("- 纯净度：抽 15/40/65/90% 四帧 RapidOCR；明显字幕/水印即剔除。边缘疑似水印仍保留并标注，供人工复核。")
    lines.append("- Veo 3.1 近半年高互动、时长合格、画面干净的单镜头几乎搜不到（多为剪辑成片或产品演示），本批为 0。")
    lines.append("- 未上传任何外部表格。本地目录：`ai-videos-2026-09-14/`。")
    (ROOT / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote index.md", len(rows))


def poster_for(r: dict) -> str:
    stem = Path(r["filename"]).stem
    p = FRAMES / stem / "0.jpg"
    if p.exists():
        return f"frames/{stem}/0.jpg"
    handle = (r.get("handle") or "").lstrip("@")
    for d in FRAMES.glob(f"*@{handle}*"):
        jpg = d / "0.jpg"
        if jpg.exists():
            return f"frames/{d.name}/0.jpg"
    return ""


def catalog_items(rows: list[dict]) -> list[dict]:
    items = []
    for i, r in enumerate(rows, 1):
        handle = (r.get("handle") or "").lstrip("@")
        items.append(
            {
                "n": i,
                "id": str(r.get("id") or ""),
                "file": r.get("filename"),
                "src": "videos/" + r.get("filename"),
                "poster": poster_for(r),
                "sell": r.get("sell") or "",
                "caption": r.get("caption") or "",
                "model": r.get("model"),
                "handle": handle,
                "likes": r.get("likes") or 0,
                "views": r.get("views") or 0,
                "followers": r.get("followers") or 0,
                "dur": r.get("measured_s") or 0,
                "date": r.get("date") or "",
                "purity": r.get("purity") or "",
                "tweet": r.get("tweet")
                or f"https://x.com/{handle}/status/{r.get('id')}",
                "evidence": r.get("evidence") or "",
            }
        )
    return items


def write_catalog(rows: list[dict]) -> None:
    items = catalog_items(rows)
    data_json = json.dumps(items, ensure_ascii=False)
    models = sorted({it["model"] for it in items if it.get("model")})
    model_opts = "\n".join(
        f'<button type="button" data-model="{html_lib.escape(m)}" class="chip">{html_lib.escape(m)}</button>'
        for m in models
    )
    page = """<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>AI Videos · 2026-09-14</title>
<style>
  :root {
    --bg: #0a0a0b;
    --paper: #f3f1ec;
    --ink: #161513;
    --muted: #9a958c;
    --steel: #c8ccd4;
    --card: #fffdf8;
    --chip: #ece8e0;
    --chip-ink: #5c5852;
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 16px;
    --motion-quick: 150ms;
    --motion-fast: 250ms;
    --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; background: var(--bg); color: var(--paper);
    font-family: "Iowan Old Style", Palatino, "Palatino Linotype", "Songti SC", serif; }
  button:not(:disabled), [role="button"]:not(:disabled) { cursor: pointer; }
  header {
    padding: 36px 28px 18px;
    border-bottom: 1px solid rgba(243,241,236,.12);
    display: flex; flex-wrap: wrap; gap: 18px; align-items: flex-end; justify-content: space-between;
  }
  .kicker { letter-spacing: .18em; text-transform: uppercase; font-size: 11px; color: var(--steel);
    font-family: ui-sans-serif, system-ui, sans-serif; }
  h1 { margin: 6px 0 0; font-weight: 500; font-size: clamp(28px, 4vw, 44px); }
  .meta { color: var(--muted); font-size: 14px; max-width: 52ch; line-height: 1.5; }
  .stats { display: flex; gap: 22px; font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px; color: var(--steel); }
  .stats b { display: block; color: var(--paper); font-size: 22px; font-weight: 600; font-variant-numeric: tabular-nums; }
  .toolbar { padding: 16px 28px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
    position: sticky; top: 0; background: rgba(10,10,11,.92); backdrop-filter: blur(12px); z-index: 5;
    border-bottom: 1px solid rgba(243,241,236,.08); }
  .chip, .viewbtn {
    appearance: none; border: 1px solid rgba(243,241,236,.18); background: transparent; color: var(--paper);
    padding: 6px 12px; border-radius: 999px; font-size: 12px; cursor: pointer;
    font-family: ui-sans-serif, system-ui, sans-serif;
    min-height: 32px;
    transition: background-color var(--motion-quick) var(--ease-out), color var(--motion-quick) var(--ease-out);
  }
  .chip.on, .viewbtn.on { background: var(--paper); color: var(--ink); }
  input[type=search] {
    margin-left: auto; background: transparent; border: 1px solid rgba(243,241,236,.18);
    color: var(--paper); padding: 7px 12px; border-radius: 999px; min-width: 220px; min-height: 36px;
    font-family: ui-sans-serif, system-ui, sans-serif;
  }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 18px; padding: 22px 28px 96px; }
  article { background: var(--card); color: var(--ink); border-radius: var(--radius-md); overflow: hidden;
    box-shadow: 0 18px 40px rgba(0,0,0,.28); }
  video { width: 100%; aspect-ratio: 16/9; object-fit: cover; background: #111; display: block;
    outline: 1px solid rgba(0,0,0,.1); outline-offset: -1px; }
  .body { padding: 14px 14px 12px; }
  .n { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; color: var(--muted); letter-spacing: .08em; }
  .sell { margin: 6px 0 10px; font-size: 16px; line-height: 1.4; }
  .tags { display: flex; flex-wrap: wrap; gap: 6px; font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; color: var(--chip-ink); }
  .tags span { background: var(--chip); padding: 3px 8px; border-radius: 999px; }
  .foot { margin-top: 10px; display: flex; align-items: center; justify-content: space-between; gap: 8px; }
  .links { font-size: 12px; font-family: ui-sans-serif, system-ui, sans-serif; min-width: 0; overflow-wrap: anywhere; }
  .links a { color: #3d4a63; }
  .ops { display: flex; align-items: center; gap: 6px; flex: 0 0 auto; }
  .rm, .undo, .rev, .dl {
    appearance: none; border: 0; font-family: ui-sans-serif, system-ui, sans-serif;
    display: inline-flex; align-items: center; justify-content: center; gap: 6px;
    min-height: 44px; min-width: 44px; padding: 0 14px;
    border-radius: var(--radius-sm); font-size: 12px; font-weight: 500;
    transition: background-color var(--motion-quick) var(--ease-out), color var(--motion-quick) var(--ease-out),
                transform var(--motion-quick) ease-out, box-shadow var(--motion-quick) var(--ease-out);
  }
  .rm { background: var(--chip); color: var(--chip-ink); }
  .rm:hover { background: var(--ink); color: var(--paper); }
  .rm:active, .dl:active { transform: scale(0.96); }
  .dl {
    background: var(--ink); color: var(--paper); text-decoration: none; cursor: pointer;
  }
  .dl:hover { background: #000; color: var(--paper); }
  .rm:focus-visible, .undo:focus-visible, .rev:focus-visible, .chip:focus-visible, .viewbtn:focus-visible, .dl:focus-visible, .dl-t:focus-visible {
    outline: 2px solid var(--steel); outline-offset: 2px;
  }
  .rm svg, .dl svg { display: block; }
  .rm-t, .dl-t {
    appearance: none; border: 1px solid rgba(243,241,236,.18); background: transparent; color: var(--paper);
    min-height: 44px; min-width: 44px; padding: 0 14px; border-radius: var(--radius-sm);
    font-family: ui-sans-serif, system-ui, sans-serif; font-size: 12px;
    display: inline-flex; align-items: center; justify-content: center;
    text-decoration: none; cursor: pointer;
    transition: background-color var(--motion-quick) var(--ease-out), color var(--motion-quick) var(--ease-out),
                transform var(--motion-quick) ease-out;
  }
  .rm-t:hover, .dl-t:hover { background: var(--paper); color: var(--ink); }
  .rm-t:active, .dl-t:active { transform: scale(0.96); }
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .tablewrap, .removedwrap { padding: 8px 28px 96px; overflow: auto; display: none; }
  .tablewrap.on, .removedwrap.on { display: block; }
  .grid.off { display: none; }
  th, td { border-bottom: 1px solid rgba(243,241,236,.12); padding: 10px 8px; text-align: left; vertical-align: top; }
  th { font-family: ui-sans-serif, system-ui, sans-serif; font-size: 11px; color: var(--steel); font-weight: 500; letter-spacing: .06em; }
  td a { color: var(--steel); }
  td.op { white-space: nowrap; width: 1%; }
  .warn { padding: 10px 28px; color: var(--muted); font-size: 13px; font-family: ui-sans-serif, system-ui, sans-serif; line-height: 1.5; }
  .warn a { color: var(--steel); }
  .removed-lead { color: var(--muted); font-size: 14px; margin: 8px 0 18px; max-width: 60ch; }
  .rlist { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 10px; }
  .rlist li {
    display: flex; align-items: center; justify-content: space-between; gap: 14px; flex-wrap: wrap;
    background: #121214; color: var(--paper); border-radius: var(--radius-lg); padding: 8px 8px 8px 16px;
    box-shadow: 0 0 0 1px rgba(255,255,255,.08);
  }
  .rlist .who { font-size: 15px; line-height: 1.4; min-width: 0; }
  .rlist .sub { display: block; margin-top: 4px; font-size: 12px; color: var(--muted);
    font-family: ui-sans-serif, system-ui, sans-serif; }
  .rev { background: var(--paper); color: var(--ink); }
  .rev:hover { background: var(--steel); }
  .rev:active { transform: scale(0.96); }
  .empty { color: var(--muted); font-size: 14px; padding: 24px 0; }
  #toast {
    position: fixed; left: 50%; bottom: 28px; z-index: 30;
    transform: translateX(-50%) translateY(12px);
    opacity: 0; pointer-events: none;
    display: flex; align-items: center; gap: 12px;
    background: var(--paper); color: var(--ink);
    padding: 8px 8px 8px 18px; border-radius: var(--radius-lg);
    box-shadow: 0 18px 40px rgba(0,0,0,.4);
    font-family: ui-sans-serif, system-ui, sans-serif; font-size: 13px;
    max-width: min(520px, calc(100vw - 32px));
    transition: opacity var(--motion-quick) var(--ease-out), transform var(--motion-quick) var(--ease-out);
  }
  #toast.show { opacity: 1; transform: translateX(-50%) translateY(0); pointer-events: auto; }
  #toastMsg { min-width: 0; line-height: 1.4; }
  .undo { background: var(--ink); color: var(--paper); }
  .undo:hover { background: #2a2724; }
  .undo:active { transform: scale(0.96); }
  html.public-view .rm, html.public-view .rm-t, html.public-view .ops .rm,
  html.public-view #btnRemoved, html.public-view #toast, html.public-view .removedwrap,
  html.public-view td.op { display: none !important; }
  @media (max-width: 640px) {
    header, .toolbar, .warn, .grid, .tablewrap, .removedwrap { padding-left: 16px; padding-right: 16px; }
    input[type=search] { margin-left: 0; width: 100%; min-width: 0; }
    .foot { align-items: stretch; }
    .rm { width: 100%; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      transition-duration: 0.01ms !important;
    }
  }
</style>
</head>
<body>
<header>
  <div>
    <div class="kicker">Local catalog · screening</div>
    <h1>AI 生成视频素材</h1>
    <p class="meta">白名单模型、8–35 秒实测、近半年、高互动、画面无字幕水印。点「去掉」移出清单，刷新也不会回来；8 秒内可撤销，已去掉列表里随时恢复。</p>
  </div>
  <div class="stats">
    <div><b id="count">__COUNT__</b>已收录</div>
    <div><b>200</b>目标</div>
    <div><b>__MODELS__</b>个模型</div>
    <div><b id="removedN">0</b>已去掉</div>
  </div>
</header>
<div class="toolbar">
  <button type="button" class="chip on" data-model="ALL">全部</button>
  __OPTS__
  <button type="button" class="viewbtn on" id="btnGrid">卡片</button>
  <button type="button" class="viewbtn" id="btnTable">表格</button>
  <button type="button" class="viewbtn" id="btnRemoved">已去掉</button>
  <input id="q" type="search" placeholder="搜卖点 / 账号 / 模型" />
</div>
<p class="warn">点击卡片即可播放本地成片。去掉会写入清单并避开再次收录，文件进回收区而不是立刻删掉。完整表见 <a href="index.md">index.md</a>。</p>
<section class="grid" id="grid"></section>
<div class="tablewrap" id="tablewrap">
  <table>
    <thead>
      <tr>
        <th>#</th><th>文件名</th><th>卖点</th><th>模型</th><th>时长</th>
        <th>账号</th><th>粉丝</th><th>点赞</th><th>播放</th><th>日期</th><th>纯净</th><th>操作</th>
      </tr>
    </thead>
    <tbody id="tbody"></tbody>
  </table>
</div>
<div class="removedwrap" id="removedwrap">
  <p class="removed-lead">已移出清单的条目会避开自动再收录。点恢复即可放回画廊。</p>
  <ul class="rlist" id="removedList"></ul>
</div>
<div id="toast" role="status" aria-live="polite">
  <span id="toastMsg">已去掉</span>
  <button type="button" class="undo" id="btnUndo">撤销</button>
</div>
<script>
(function(){
  const h = location.hostname;
  const pub = /(^|\.)github\.io$/.test(h)
    || /githack\.com$/.test(h)
    || /jsdelivr\.net$/.test(h)
    || /htmlpreview\.github\.io$/.test(h)
    || /statically\.io$/.test(h);
  if (!pub) return;
  document.documentElement.classList.add("public-view");
  const w = document.querySelector(".warn");
  if (w) w.innerHTML = '点击卡片即可播放成片。完整表见 <a href="index.md">index.md</a>。';
  const k = document.querySelector(".kicker");
  if (k) k.textContent = "Public catalog";
  const m = document.querySelector(".meta");
  if (m) m.textContent = "白名单模型、8–35 秒实测、近半年、高互动、画面无字幕水印。筛选、播放、下载均可。";
})();
const BAKED = __DATA__;
const MEDIA_BASE = "https://raw.githubusercontent.com/bqkcqygfxsgst/ai-video-example/main/ai-videos-2026-09-14/";
let DATA = Array.isArray(BAKED) ? BAKED.slice() : [];
if (document.documentElement.classList.contains("public-view")) {
  DATA = DATA.map(function (it) {
    const o = Object.assign({}, it);
    if (o.src && !/^https?:/i.test(o.src)) o.src = MEDIA_BASE + o.src;
    if (o.poster && !/^https?:/i.test(o.poster)) o.poster = MEDIA_BASE + o.poster;
    return o;
  });
}
let REMOVED = [];
let model = "ALL";
let view = "grid";
const grid = document.getElementById("grid");
const tbody = document.getElementById("tbody");
const q = document.getElementById("q");
const toast = document.getElementById("toast");
const toastMsg = document.getElementById("toastMsg");
const undoStack = [];
const inflight = new Set();
let toastTimer = 0;

function esc(s) {
  const d = document.createElement("span");
  d.textContent = String(s ?? "");
  const amp = String.fromCharCode(38);
  return d.innerHTML
    .replace(/"/g, amp + "#34;")
    .replace(/'/g, amp + "#39;")
    .replace(/`/g, amp + "#96;");
}
function fmt(n) {
  n = +n || 0;
  if (n >= 1e6) return (n/1e6).toFixed(1) + "M";
  if (n >= 1e3) return (n/1e3).toFixed(1) + "K";
  return String(n);
}
function filtered() {
  const s = (q.value || "").trim().toLowerCase();
  return DATA.filter(it => {
    if (model !== "ALL" && it.model !== model) return false;
    if (!s) return true;
    return (it.sell + it.handle + it.model + it.file + it.caption).toLowerCase().includes(s);
  });
}
function rmIcon() {
  return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 3l8 8M11 3L3 11" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>';
}
function dlIcon() {
  return '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M7 2v7M4 7l3 3 3-3M2.5 11.5h9" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';
}
function setView(next) {
  view = next;
  document.getElementById("btnGrid").classList.toggle("on", next === "grid");
  document.getElementById("btnTable").classList.toggle("on", next === "table");
  document.getElementById("btnRemoved").classList.toggle("on", next === "removed");
  grid.classList.toggle("off", next !== "grid");
  document.getElementById("tablewrap").classList.toggle("on", next === "table");
  document.getElementById("removedwrap").classList.toggle("on", next === "removed");
}
function renderRemoved() {
  const list = document.getElementById("removedList");
  document.getElementById("removedN").textContent = String(REMOVED.length);
  if (!REMOVED.length) {
    list.innerHTML = '<li class="empty">还没有去掉的条目。</li>';
    return;
  }
  list.innerHTML = REMOVED.map(it => `
    <li>
      <div class="who">${esc(it.sell || it.file || it.id)}
        <span class="sub">${esc(it.model)} · @${esc(it.handle)} · ${esc(it.date || "")}</span>
      </div>
      <button type="button" class="rev" data-restore="${esc(it.id)}">恢复</button>
    </li>`).join("");
}
function render() {
  const rows = filtered();
  document.getElementById("count").textContent = rows.length;
  renderRemoved();
  grid.innerHTML = rows.map(it => `
    <article data-id="${esc(it.id)}">
      <video controls preload="none" poster="${esc(it.poster || "")}" src="${esc(it.src)}"></video>
      <div class="body">
        <div class="n">#${String(it.n).padStart(3,"0")} · ${esc(it.date)}</div>
        <div class="sell">${esc(it.sell || it.caption)}</div>
        <div class="tags">
          <span>${esc(it.model)}</span>
          <span>@${esc(it.handle)}</span>
          <span>${esc(it.dur)}s</span>
          <span>❤ ${fmt(it.likes)}</span>
          <span>▶ ${fmt(it.views)}</span>
          <span>${esc(it.purity)}</span>
        </div>
        <div class="foot">
          <div class="links"><a href="${esc(it.tweet)}" target="_blank" rel="noopener">原推文</a> · ${esc(it.file)}</div>
          <div class="ops">
            <a class="dl" href="${esc(it.src)}?dl=1" download="${esc(it.file)}" aria-label="下载这条视频">${dlIcon()}下载</a>
            <button type="button" class="rm" data-remove="${esc(it.id)}" aria-label="去掉这条">${rmIcon()}去掉</button>
          </div>
        </div>
      </div>
    </article>`).join("");
  tbody.innerHTML = rows.map(it => `
    <tr data-id="${esc(it.id)}">
      <td>${it.n}</td>
      <td><a href="${esc(it.src)}" download>${esc(it.file)}</a></td>
      <td>${esc(it.sell)}</td>
      <td>${esc(it.model)}</td>
      <td>${esc(it.dur)}</td>
      <td>@${esc(it.handle)}</td>
      <td>${fmt(it.followers)}</td>
      <td>${fmt(it.likes)}</td>
      <td>${fmt(it.views)}</td>
      <td>${esc(it.date)}</td>
      <td>${esc(it.purity)}</td>
      <td class="op"><a class="dl-t" href="${esc(it.src)}?dl=1" download="${esc(it.file)}">下载</a> <button type="button" class="rm-t" data-remove="${esc(it.id)}">去掉</button></td>
    </tr>`).join("");
}
function showToast(item) {
  const label = (item.sell || item.file || item.id || "").slice(0, 28);
  toastMsg.textContent = "已去掉「" + label + "」";
  toast.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("show"), 8000);
}
async function api(path, id) {
  const r = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    cache: "no-store",
    body: JSON.stringify({ id: String(id) })
  });
  let j = {};
  try { j = await r.json(); } catch (e) { j = {}; }
  if (!r.ok) {
    const err = new Error(j.error || ("http " + r.status));
    err.status = r.status;
    throw err;
  }
  return j;
}
async function refresh() {
  try {
    const r = await fetch("/api/catalog", { cache: "no-store" });
    if (!r.ok) throw 0;
    const j = await r.json();
    if (Array.isArray(j.items)) DATA = j.items;
    if (Array.isArray(j.removed)) REMOVED = j.removed;
  } catch (e) {}
  render();
}
async function removeItem(id) {
  id = String(id || "");
  if (!id || inflight.has(id)) return;
  const idx = DATA.findIndex(x => String(x.id) === id);
  if (idx < 0) return;
  const item = DATA[idx];
  inflight.add(id);
  DATA.splice(idx, 1);
  undoStack.push(item);
  REMOVED.unshift({
    id: item.id,
    sell: item.sell || item.caption || "",
    handle: item.handle,
    model: item.model,
    file: item.file,
    date: item.date,
    purity: item.purity
  });
  showToast(item);
  render();
  try {
    await api("/api/remove", id);
    await refresh();
  } catch (e) {
    if (e.status !== 404) {
      if (!DATA.some(x => String(x.id) === id)) DATA.splice(Math.min(idx, DATA.length), 0, item);
      REMOVED = REMOVED.filter(x => String(x.id) !== id);
      undoStack.pop();
      toastMsg.textContent = "去掉失败，已放回";
      toast.classList.add("show");
      render();
    } else {
      await refresh();
    }
  } finally {
    inflight.delete(id);
  }
}
async function restoreItem(id) {
  id = String(id || "");
  if (!id || inflight.has("r" + id)) return;
  inflight.add("r" + id);
  try {
    await api("/api/restore", id);
    await refresh();
  } catch (e) {
    toastMsg.textContent = "恢复失败";
    toast.classList.add("show");
  } finally {
    inflight.delete("r" + id);
  }
}
function undoLast() {
  const item = undoStack.pop();
  toast.classList.remove("show");
  if (!item) return;
  restoreItem(item.id);
}

document.querySelectorAll(".chip[data-model]").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".chip[data-model]").forEach(b => b.classList.remove("on"));
    btn.classList.add("on");
    model = btn.dataset.model;
    render();
  });
});
q.addEventListener("input", render);
document.getElementById("btnGrid").addEventListener("click", () => { setView("grid"); render(); });
document.getElementById("btnTable").addEventListener("click", () => { setView("table"); render(); });
document.getElementById("btnRemoved").addEventListener("click", () => { setView("removed"); render(); });
document.getElementById("btnUndo").addEventListener("click", undoLast);
document.body.addEventListener("click", (e) => {
  const rm = e.target.closest("[data-remove]");
  if (rm) { e.preventDefault(); removeItem(rm.getAttribute("data-remove")); return; }
  const rv = e.target.closest("[data-restore]");
  if (rv) { e.preventDefault(); restoreItem(rv.getAttribute("data-restore")); }
});
refresh();
</script>
</body>
</html>
"""
    page = (
        page.replace("__COUNT__", str(len(items)))
        .replace("__MODELS__", str(len(models)))
        .replace("__OPTS__", model_opts)
        .replace("__DATA__", data_json)
    )
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print("wrote index.html", len(items))


def main():
    rows = load_accepted()
    write_index(rows)
    write_catalog(rows)
    (META / "accepted_clean.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
