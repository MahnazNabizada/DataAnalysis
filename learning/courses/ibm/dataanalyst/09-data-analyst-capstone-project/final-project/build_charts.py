"""Generate every chart used in the Data Analyst Capstone Project Report deck.

Reads the same lab artefacts produced across modules 1-5 of the capstone and
writes PNGs into final-project/assets/. Also prints the figures quoted on the
slides so the narrative and the visuals cannot drift apart.
"""

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

HANDS_ON = os.path.join(
    r"D:\Developer\DataAnalysis\learning\courses\ibm\dataanalyst",
    r"09-data-analyst-capstone-project\activities\hands-on",
)
DASH = os.path.join(HANDS_ON, "25-building-dashboard-google-locker")
OUT = os.path.join(
    r"D:\Developer\DataAnalysis\learning\courses\ibm\dataanalyst",
    r"09-data-analyst-capstone-project\final-project\assets",
)
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- design tokens
# Matched to the deck's "IBM Skills Network" theme: accent1 purple leads, with
# the validated orange / aqua as slots 2-3. Surface is the slides' own white so
# the PNGs sit flush on the page. Palette checked with the dataviz validator
# (all-pairs CVD dE 9.2, normal-vision 27.6, on a #ffffff surface).
SURFACE = "#ffffff"
INK = "#262626"
INK2 = "#525252"
MUTED = "#8d8d8d"
GRID = "#e8e8e8"
BASELINE = "#c6c6c6"
BLUE = "#6c4dea"   # slot 1 - theme accent1
ORANGE = "#eb6834"  # slot 2 - next year / desired
AQUA = "#1baf7a"    # slot 3 - secondary dimension
RED = "#d03b3b"     # diverging negative arm
SEQ = ["#ded6fc", "#c3b4f8", "#a48ff2", "#8469ec", "#6c4dea", "#5334c4", "#3d2593"]

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "DejaVu Sans"],
    "text.color": INK,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": INK2,
    "axes.edgecolor": BASELINE,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "font.size": 10,
    "figure.dpi": 200,
})

facts = {}


def strip_frame(ax, keep=()):
    for side in ("top", "right", "bottom", "left"):
        if side not in keep:
            ax.spines[side].set_visible(False)


def hbar(ax, labels, values, color=BLUE, fmt="{:,.0f}", title=None, pad=0.16):
    """Ranked horizontal bars: largest on top, value direct-labelled at the end."""
    y = np.arange(len(labels))
    ax.barh(y, values, color=color, height=0.68, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlim(0, max(values) * (1 + pad))
    ax.set_xticks([])
    strip_frame(ax)
    ax.tick_params(axis="y", length=0)
    for yi, v in zip(y, values):
        ax.text(v + max(values) * 0.015, yi, fmt.format(v), va="center",
                ha="left", fontsize=9, color=INK2)
    if title:
        ax.set_title(title, loc="left", color=INK, pad=8)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print("  wrote", name)


def explode(series):
    return series.dropna().str.split(";").explode().str.strip().value_counts()


# The survey spells countries out in full; the long forms blow out chart margins.
COUNTRY_SHORT = {
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Russian Federation": "Russia",
    "Iran, Islamic Republic of...": "Iran",
    "Venezuela, Bolivarian Republic of...": "Venezuela",
    "Republic of Korea": "South Korea",
    "Viet Nam": "Vietnam",
    "United Republic of Tanzania": "Tanzania",
}


def short_country(name):
    return COUNTRY_SHORT.get(name, name)


# =============================================================== MODULE 1 DATA
print("\n== Module 1: data collection ==")
jobs = pd.read_excel(os.path.join(HANDS_ON, "02-collecting-data-using-apis",
                                  "job-postings.xlsx"))
jobs = jobs.sort_values("Number Job Postings", ascending=False)
facts["job_total"] = int(jobs["Number Job Postings"].sum())
facts["job_top"] = (jobs.iloc[0]["Location"], int(jobs.iloc[0]["Number Job Postings"]))
facts["job_top3_share"] = round(
    100 * jobs["Number Job Postings"].head(3).sum() / facts["job_total"], 1)
facts["job_bottom"] = (jobs.iloc[-1]["Location"], int(jobs.iloc[-1]["Number Job Postings"]))
facts["job_n_loc"] = len(jobs)

fig, ax = plt.subplots(figsize=(7.6, 4.6))
hbar(ax, jobs["Location"].tolist(), jobs["Number Job Postings"].tolist(),
     title="Python job postings by location  ·  Jobs API, 13 metro areas")
ax.set_xlabel("Number of job postings")
save(fig, "r1_job_postings.png")

skills = pd.read_excel(os.path.join(HANDS_ON, "02-collecting-data-using-apis",
                                    "skills-job-postings.xlsx"))
skills = skills.sort_values("Number Job Postings", ascending=False)
facts["skills_top"] = [(r.Skill, int(r._2)) for r in skills.head(4).itertuples()]
fig, ax = plt.subplots(figsize=(7.4, 4.3))
hbar(ax, skills["Skill"].tolist(), skills["Number Job Postings"].tolist(),
     color=AQUA, title="Job postings by required technology  ·  Jobs API")
ax.set_xlabel("Number of job postings")
save(fig, "a1_job_postings_by_skill.png")

langs_sal = pd.read_csv(os.path.join(HANDS_ON, "04-collecting-data-using-web-scraping",
                                     "popular-languages.csv"))
langs_sal["salary"] = (langs_sal["Annual Average Salary"]
                       .str.replace(r"[\$,]", "", regex=True).astype(float))
langs_sal = langs_sal.sort_values("salary", ascending=False)
facts["sal_top"] = (langs_sal.iloc[0]["Language"], int(langs_sal.iloc[0]["salary"]))
facts["sal_bottom"] = (langs_sal.iloc[-1]["Language"], int(langs_sal.iloc[-1]["salary"]))
facts["sal_spread"] = int(langs_sal.iloc[0]["salary"] - langs_sal.iloc[-1]["salary"])
facts["sal_python"] = int(langs_sal.set_index("Language").loc["Python", "salary"])
facts["sal_mean"] = int(langs_sal["salary"].mean())

fig, ax = plt.subplots(figsize=(7.6, 4.4))
hbar(ax, langs_sal["Language"].tolist(), langs_sal["salary"].tolist(),
     fmt="${:,.0f}", pad=0.20,
     title="Annual average salary by programming language  ·  web-scraped, 10 languages")
ax.set_xlabel("Annual average salary (USD)")
save(fig, "r2_language_salary.png")

# =============================================================== SURVEY DATA
print("\n== Modules 2-5: Stack Overflow survey ==")
df = pd.read_csv(os.path.join(DASH, "survey_data_updated.csv"), low_memory=False)
df.columns = df.columns.str.strip().str.replace(r"\s+", " ", regex=True)
facts["rows"], facts["cols"] = df.shape
facts["countries"] = int(df["Country"].nunique())

pairs = {
    "Language": ("LanguageHaveWorkedWith", "LanguageWantToWorkWith"),
    "Database": ("DatabaseHaveWorkedWith", "DatabaseWantToWorkWith"),
    "Platform": ("PlatformHaveWorkedWith", "PlatformWantToWorkWith"),
    "Webframe": ("WebframeHaveWorkedWith", "WebframeWantToWorkWith"),
}
counts = {k: (explode(df[a]), explode(df[b])) for k, (a, b) in pairs.items()}

for key, (have, want) in counts.items():
    facts[f"{key}_have_top5"] = [(i, int(v)) for i, v in have.head(5).items()]
    facts[f"{key}_want_top5"] = [(i, int(v)) for i, v in want.head(5).items()]

# ---- Results: top 10 languages, current vs next year
for key, (have, want), c_now, c_next in [
    ("lang", counts["Language"], BLUE, ORANGE),
    ("db", counts["Database"], BLUE, ORANGE),
]:
    for tag, s, color, ttl in [
        ("now", have.head(10), c_now, "Current year — have worked with"),
        ("next", want.head(10), c_next, "Next year — want to work with"),
    ]:
        fig, ax = plt.subplots(figsize=(5.9, 4.3))
        hbar(ax, s.index.tolist(), s.values.tolist(), color=color, title=ttl)
        ax.set_xlabel("Respondents")
        save(fig, f"r3_{key}_{tag}.png")

# ---- Net change (diverging): desired vs current.
# Raw count differences are biased. Respondents tick fewer boxes on the
# "want to work with" question than on "have worked with" (6.19 vs 5.64
# languages on average), so subtracting raw counts pushes nearly every
# technology negative regardless of real sentiment. Normalising each side to a
# share of all selections made on that question removes the bias and leaves a
# percentage-point shift in mind-share that is comparable across technologies.
for key, label, fname in [("Language", "programming language", "r4_lang_netchange.png"),
                          ("Database", "database", "r4_db_netchange.png")]:
    have, want = counts[key]
    tot_have, tot_want = int(have.sum()), int(want.sum())
    facts[f"{key}_sel_have"], facts[f"{key}_sel_want"] = tot_have, tot_want
    facts[f"{key}_per_resp"] = (round(tot_have / facts["rows"], 2),
                                round(tot_want / facts["rows"], 2))

    universe = have.head(12).index.union(want.head(12).index)
    share_have = 100 * have.reindex(universe).fillna(0) / tot_have
    share_want = 100 * want.reindex(universe).fillna(0) / tot_want
    delta = (share_want - share_have).sort_values()
    facts[f"{key}_gainers"] = [(i, round(v, 1)) for i, v in delta[delta > 0][::-1].head(4).items()]
    facts[f"{key}_losers"] = [(i, round(v, 1)) for i, v in delta[delta < 0].head(4).items()]

    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    colors = [RED if v < 0 else BLUE for v in delta.values]
    y = np.arange(len(delta))
    ax.barh(y, delta.values, color=colors, height=0.7, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(delta.index)
    ax.axvline(0, color=BASELINE, lw=1.2, zorder=4)
    strip_frame(ax)
    ax.tick_params(axis="y", length=0)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"{v:+.0f} pp"))
    span = max(abs(delta.min()), abs(delta.max()))
    ax.set_xlim(-span * 1.32, span * 1.32)
    for yi, v in zip(y, delta.values):
        off = span * 0.03
        ax.text(v + (off if v >= 0 else -off), yi, f"{v:+.1f}", va="center",
                ha="left" if v >= 0 else "right", fontsize=9, color=INK2)
    ax.set_title(f"Net mind-share shift by {label}\nwant to work with − have worked with, "
                 f"each as a share of all selections on that question",
                 loc="left", color=INK, pad=8, fontsize=12)
    ax.set_xlabel("Change in share of selections (percentage points)")
    save(fig, fname)

# ---- Dashboard tab 1: current technology usage
def dash_panel(fname, series_specs, header, sub):
    fig = plt.figure(figsize=(12.2, 6.1))
    fig.patch.set_facecolor(SURFACE)
    fig.text(0.012, 0.975, header, fontsize=17, fontweight="bold", color=INK, va="top")
    fig.text(0.012, 0.925, sub, fontsize=10.5, color=INK2, va="top")
    n = len(series_specs)
    rows, cols = (2, 2) if n == 4 else (1, 3)
    gs = fig.add_gridspec(rows, cols, top=0.855, bottom=0.055, left=0.055,
                          right=0.985, hspace=0.30, wspace=0.34)
    for i, (ttl, s, color, kind) in enumerate(series_specs):
        ax = fig.add_subplot(gs[i // cols, i % cols])
        if kind == "hbar":
            hbar(ax, list(s.index), list(s.values), color=color, title=ttl)
        else:  # vertical bars, ordinal categories
            x = np.arange(len(s))
            ax.bar(x, s.values, color=color, width=0.7, zorder=3)
            ax.set_xticks(x)
            ax.set_xticklabels(s.index, rotation=28, ha="right", fontsize=8.5)
            ax.set_yticks([])
            strip_frame(ax)
            ax.tick_params(length=0)
            for xi, v in zip(x, s.values):
                ax.text(xi, v + max(s.values) * 0.02, f"{v:,.0f}", ha="center",
                        va="bottom", fontsize=8, color=INK2)
            ax.set_ylim(0, max(s.values) * 1.16)
            ax.set_title(ttl, loc="left", color=INK, fontsize=12, pad=8)
    fig.savefig(os.path.join(OUT, fname), bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)
    print("  wrote", fname)


sub_note = f"Stack Overflow Developer Survey · {facts['rows']:,} respondents · multi-select, respondents may pick several"
dash_panel("d1_current_usage.png", [
    ("Top 10 languages", counts["Language"][0].head(10), BLUE, "hbar"),
    ("Top 10 databases", counts["Database"][0].head(10), BLUE, "hbar"),
    ("Top 10 platforms", counts["Platform"][0].head(10), BLUE, "hbar"),
    ("Top 10 web frameworks", counts["Webframe"][0].head(10), BLUE, "hbar"),
], "DASHBOARD TAB 1 — CURRENT TECHNOLOGY USAGE", sub_note)

dash_panel("d2_future_trends.png", [
    ("Top 10 languages desired next year", counts["Language"][1].head(10), ORANGE, "hbar"),
    ("Top 10 databases desired next year", counts["Database"][1].head(10), ORANGE, "hbar"),
    ("Top 10 platforms desired next year", counts["Platform"][1].head(10), ORANGE, "hbar"),
    ("Top 10 web frameworks desired next year", counts["Webframe"][1].head(10), ORANGE, "hbar"),
], "DASHBOARD TAB 2 — FUTURE TECHNOLOGY TRENDS", sub_note)

# ---- Demographics
country = df["Country"].value_counts().head(10)
country.index = [short_country(i) for i in country.index]
age_order = ["Under 18 years old", "18-24 years old", "25-34 years old",
             "35-44 years old", "45-54 years old", "55-64 years old",
             "65 years or older", "Prefer not to say"]
age = df["Age"].value_counts().reindex(age_order).dropna()
age.index = [i.replace(" years old", "").replace(" years or older", "+") for i in age.index]
ed_short = {
    "Bachelor's degree (B.A., B.S., B.Eng., etc.)": "Bachelor's",
    "Master's degree (M.A., M.S., M.Eng., MBA, etc.)": "Master's",
    "Some college/university study without earning a degree": "Some college",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": "Secondary school",
    "Professional degree (JD, MD, Ph.D, Ed.D, etc.)": "Professional / PhD",
    "Associate degree (A.A., A.S., etc.)": "Associate",
    "Primary/elementary school": "Primary school",
    "Something else": "Something else",
}
ed = df["EdLevel"].value_counts()
# The survey export uses a curly apostrophe; normalise before matching.
ed.index = [ed_short.get(str(i).replace("’", "'"), i) for i in ed.index]

facts["country_top5"] = [(i, int(v)) for i, v in country.head(5).items()]
facts["country_top5_share"] = round(100 * country.head(5).sum() / df["Country"].notna().sum(), 1)
facts["age_top"] = (age.index[age.argmax()], int(age.max()))
facts["age_2534_share"] = round(100 * age.max() / age.sum(), 1)
facts["age_under35_share"] = round(
    100 * age[[i for i in age.index if i in ("Under 18", "18-24", "25-34")]].sum() / age.sum(), 1)
facts["ed_top"] = (ed.index[0], int(ed.iloc[0]))
facts["ed_degree_share"] = round(
    100 * ed[[i for i in ed.index if i in ("Bachelor's", "Master's", "Professional / PhD",
                                           "Associate")]].sum() / ed.sum(), 1)

dash_panel("d3_demographics.png", [
    ("Top 10 countries by respondents", country, AQUA, "hbar"),
    ("Respondents by age group", age, AQUA, "vbar"),
    ("Respondents by education level", ed, AQUA, "vbar"),
], "DASHBOARD TAB 3 — DEMOGRAPHICS",
    f"Stack Overflow Developer Survey · {facts['rows']:,} respondents · {facts['countries']} countries")

# =============================================================== APPENDIX
print("\n== Appendix charts ==")
comp = pd.to_numeric(df["ConvertedCompYearly"], errors="coerce")
facts["comp_valid"] = int(comp.notna().sum())
facts["comp_missing_pct"] = round(100 * comp.isna().mean(), 1)
facts["comp_median"] = int(comp.median())
facts["comp_mean"] = int(comp.mean())
q1, q3 = comp.quantile([0.25, 0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
facts["comp_iqr_upper"] = int(upper)
facts["comp_outliers"] = int(((comp > upper) | (comp < q1 - 1.5 * iqr)).sum())
facts["comp_outlier_pct"] = round(100 * facts["comp_outliers"] / facts["comp_valid"], 1)

fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.4, 4.0))
p99 = comp.quantile(0.99)
axa.hist(comp.dropna().clip(upper=p99), bins=45, color=BLUE, zorder=3)
axa.set_title("Yearly compensation (clipped at 99th percentile)", loc="left", color=INK, pad=8)
axa.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"${v/1000:.0f}k"))
axb.hist(np.log1p(comp.dropna()), bins=45, color=ORANGE, zorder=3)
axb.set_title("log1p(compensation) — skew corrected", loc="left", color=INK, pad=8)
for ax in (axa, axb):
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    strip_frame(ax)
    ax.set_ylabel("Respondents", color=INK2)
save(fig, "a2_comp_distribution.png")

top_c = df["Country"].value_counts().head(10).index
cd = df[df["Country"].isin(top_c)][["Country", "ConvertedCompYearly"]].dropna()
cd["ConvertedCompYearly"] = pd.to_numeric(cd["ConvertedCompYearly"], errors="coerce")
cd = cd.dropna()
order = cd.groupby("Country")["ConvertedCompYearly"].median().sort_values(ascending=False).index
facts["comp_country_top3"] = [(short_country(c), int(cd[cd.Country == c]["ConvertedCompYearly"].median()))
                              for c in order[:3]]
facts["comp_country_bottom"] = [(short_country(c), int(cd[cd.Country == c]["ConvertedCompYearly"].median()))
                                for c in order[-2:]]
fig, ax = plt.subplots(figsize=(8.6, 4.3))
data = [cd[cd.Country == c]["ConvertedCompYearly"].values for c in order]
bp = ax.boxplot(data, vert=False, patch_artist=True, showfliers=False, widths=0.62)
for patch in bp["boxes"]:
    patch.set_facecolor(BLUE)
    patch.set_edgecolor(SURFACE)
    patch.set_linewidth(1.6)
for el in ("whiskers", "caps"):
    for line in bp[el]:
        line.set_color(BASELINE)
for line in bp["medians"]:
    line.set_color(SURFACE)
    line.set_linewidth(1.8)
ax.set_yticklabels([short_country(c) for c in order])
ax.invert_yaxis()
ax.set_xlim(0, cd["ConvertedCompYearly"].quantile(0.985))
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"${v/1000:.0f}k"))
ax.xaxis.grid(True, zorder=0)
ax.set_axisbelow(True)
strip_frame(ax)
ax.tick_params(axis="y", length=0)
ax.set_title("Yearly compensation by country  ·  top 10 by respondent count, outliers hidden",
             loc="left", color=INK, pad=8)
ax.set_xlabel("Converted yearly compensation (USD)")
save(fig, "a3_comp_by_country.png")

# correlation heatmap
num = pd.DataFrame({
    "Compensation": comp,
    "Work exp. (yrs)": pd.to_numeric(df["WorkExp"], errors="coerce"),
    "Years coding pro": pd.to_numeric(
        df["YearsCodePro"].replace({"Less than 1 year": 0.5, "More than 50 years": 51}),
        errors="coerce"),
    "Job satisfaction": pd.to_numeric(df["JobSat"], errors="coerce"),
}).dropna()
corr = num.corr()
facts["corr_pairs"] = {
    "comp_workexp": round(corr.loc["Compensation", "Work exp. (yrs)"], 3),
    "comp_yearspro": round(corr.loc["Compensation", "Years coding pro"], 3),
    "jobsat_yearspro": round(corr.loc["Job satisfaction", "Years coding pro"], 3),
    "jobsat_comp": round(corr.loc["Job satisfaction", "Compensation"], 3),
    "n": int(len(num)),
}
fig, ax = plt.subplots(figsize=(5.9, 4.9))
im = ax.imshow(corr.values, cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
    "div", [RED, "#f0efec", BLUE]), vmin=-1, vmax=1)
ax.set_xticks(range(len(corr)), corr.columns, rotation=28, ha="right", fontsize=9)
ax.set_yticks(range(len(corr)), corr.columns, fontsize=9)
for i in range(len(corr)):
    for j in range(len(corr)):
        v = corr.values[i, j]
        ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=10,
                color="#ffffff" if abs(v) > 0.6 else INK)
strip_frame(ax)
ax.tick_params(length=0)
ax.set_title(f"Correlation matrix  ·  n = {len(num):,} complete cases",
             loc="left", color=INK, pad=10)
save(fig, "a4_correlation.png")

# median compensation by age group (line)
age_map = {"Under 18 years old": "<18", "18-24 years old": "18-24",
           "25-34 years old": "25-34", "35-44 years old": "35-44",
           "45-54 years old": "45-54", "55-64 years old": "55-64",
           "65 years or older": "65+"}
ac = df.assign(_age=df["Age"].map(age_map), _c=comp).dropna(subset=["_age", "_c"])
med = ac.groupby("_age")["_c"].median().reindex(
    ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]).dropna()
facts["comp_age_peak"] = (med.idxmax(), int(med.max()))
facts["comp_age_youngest"] = (med.index[0], int(med.iloc[0]))
fig, ax = plt.subplots(figsize=(7.4, 3.9))
ax.plot(med.index, med.values, color=BLUE, lw=2, marker="o", ms=8,
        mfc=BLUE, mec=SURFACE, mew=1.8, zorder=3)
for x, v in zip(med.index, med.values):
    ax.annotate(f"${v/1000:.0f}k", (x, v), textcoords="offset points",
                xytext=(0, 11), ha="center", fontsize=9, color=INK2)
ax.set_ylim(0, med.max() * 1.22)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"${v/1000:.0f}k"))
ax.yaxis.grid(True, zorder=0)
ax.set_axisbelow(True)
strip_frame(ax)
ax.set_title("Median yearly compensation by age group", loc="left", color=INK, pad=8)
ax.set_xlabel("Age group")
save(fig, "a5_comp_by_age.png")

# remote work composition (donut)
rw = df["RemoteWork"].value_counts()
facts["remote_pct"] = {k: round(100 * v / rw.sum(), 1) for k, v in rw.items()}
facts["remote_missing_pct"] = round(100 * df["RemoteWork"].isna().mean(), 1)
fig, ax = plt.subplots(figsize=(5.4, 4.0))
wedges, _ = ax.pie(rw.values, startangle=90, counterclock=False,
                   colors=[BLUE, ORANGE, AQUA],
                   wedgeprops=dict(width=0.42, edgecolor=SURFACE, linewidth=2))
ax.legend(wedges, [f"{k} — {100*v/rw.sum():.0f}%" for k, v in rw.items()],
          loc="center left", bbox_to_anchor=(0.98, 0.5), frameon=False, fontsize=10)
ax.set_title("Work arrangement", loc="left", color=INK, pad=8)
save(fig, "a6_remote_work.png")

# top 5 databases desired (pie, from lab 21)
d5 = counts["Database"][1].head(5)
fig, ax = plt.subplots(figsize=(5.4, 4.0))
wedges, _ = ax.pie(d5.values, startangle=90, counterclock=False,
                   colors=SEQ[5:1:-1] + [SEQ[1]],
                   wedgeprops=dict(width=0.42, edgecolor=SURFACE, linewidth=2))
ax.legend(wedges, [f"{k} — {100*v/d5.sum():.0f}%" for k, v in d5.items()],
          loc="center left", bbox_to_anchor=(0.96, 0.5), frameon=False, fontsize=10)
ax.set_title("Top 5 databases desired next year  ·  share of those five",
             loc="left", color=INK, pad=8)
save(fig, "a7_db_desired_pie.png")

# language adoption heatmap: top 10 languages x top 10 countries
lang_rows = (df[["Country", "LanguageHaveWorkedWith"]].dropna()
             .assign(L=lambda x: x["LanguageHaveWorkedWith"].str.split(";"))
             .explode("L").reset_index(drop=True))
lang_rows["L"] = lang_rows["L"].str.strip()
top10l = counts["Language"][0].head(10).index
sub = lang_rows[lang_rows["Country"].isin(top_c) & lang_rows["L"].isin(top10l)]
ct = pd.crosstab(sub["Country"], sub["L"], normalize="index") * 100
ct = ct.reindex(index=top_c, columns=top10l)
fig, ax = plt.subplots(figsize=(9.0, 4.4))
im = ax.imshow(ct.values, cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
    "seq", SEQ), vmin=0, vmax=ct.values.max())
ax.set_xticks(range(len(ct.columns)), ct.columns, rotation=30, ha="right", fontsize=9)
ax.set_yticks(range(len(ct.index)), [short_country(c) for c in ct.index], fontsize=9)
for i in range(ct.shape[0]):
    for j in range(ct.shape[1]):
        v = ct.values[i, j]
        ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=8,
                color="#ffffff" if v > ct.values.max() * 0.62 else INK)
strip_frame(ax)
ax.tick_params(length=0)
ax.set_title("Language adoption by country  ·  % of that country's respondents",
             loc="left", color=INK, pad=10)
save(fig, "a8_language_by_country.png")

# job satisfaction distribution
js = pd.to_numeric(df["JobSat"], errors="coerce").dropna()
facts["jobsat_n"] = int(len(js))
facts["jobsat_missing_pct"] = round(100 * pd.to_numeric(df["JobSat"], errors="coerce").isna().mean(), 1)
facts["jobsat_median"] = float(js.median())
facts["jobsat_mean"] = round(float(js.mean()), 2)
facts["jobsat_7plus"] = round(100 * (js >= 7).mean(), 1)
fig, ax = plt.subplots(figsize=(7.2, 3.7))
vc = js.round().value_counts().sort_index()
ax.bar(vc.index, vc.values, color=BLUE, width=0.72, zorder=3)
for x, v in zip(vc.index, vc.values):
    ax.text(x, v + vc.max() * 0.02, f"{v:,}", ha="center", va="bottom",
            fontsize=8, color=INK2)
ax.set_ylim(0, vc.max() * 1.14)
ax.set_xticks(range(0, 11))
ax.set_yticks([])
strip_frame(ax)
ax.tick_params(length=0)
ax.set_title(f"Job satisfaction, 0–10  ·  {len(js):,} respondents who answered",
             loc="left", color=INK, pad=8)
ax.set_xlabel("Job satisfaction score")
save(fig, "a9_jobsat.png")

# data-quality: missing values in the columns that drove the wrangling decisions
key_cols = ["ConvertedCompYearly", "JobSat", "RemoteWork", "YearsCodePro",
            "WorkExp", "EdLevel", "Country", "Employment", "Age",
            "DatabaseHaveWorkedWith", "LanguageHaveWorkedWith"]
miss = (df[key_cols].isna().mean() * 100).sort_values(ascending=False)
facts["dupes_response_id"] = int(df["ResponseId"].duplicated().sum())
facts["dupes_full_row"] = int(df.duplicated().sum())
facts["miss_top"] = [(i, round(v, 1)) for i, v in miss.head(5).items()]
fig, ax = plt.subplots(figsize=(7.6, 4.3))
hbar(ax, miss.index.tolist(), miss.values.tolist(), color=ORANGE,
     fmt="{:.1f}%", pad=0.14,
     title="Missing values in the columns that drove wrangling decisions")
ax.set_xlabel("% of rows missing")
save(fig, "a10_missing_values.png")

# ---- headline current-vs-desired grouped bar (used on the discussion slide)
have, want = counts["Language"]
top8 = have.head(8).index
fig, ax = plt.subplots(figsize=(8.8, 4.2))
x = np.arange(len(top8))
w = 0.39
ax.bar(x - w / 2 - 0.01, have.reindex(top8).values, width=w, color=BLUE,
       label="Have worked with", zorder=3)
ax.bar(x + w / 2 + 0.01, want.reindex(top8).values, width=w, color=ORANGE,
       label="Want to work with", zorder=3)
ax.set_xticks(x, top8, rotation=22, ha="right", fontsize=9)
ax.yaxis.grid(True, zorder=0)
ax.set_axisbelow(True)
strip_frame(ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"{v/1000:.0f}k"))
ax.legend(frameon=False, loc="upper right", fontsize=9.5)
ax.set_title("Current use vs. next-year intent  ·  top 8 languages",
             loc="left", color=INK, pad=8)
ax.set_ylabel("Respondents")
save(fig, "a11_lang_have_vs_want.png")

with open(os.path.join(OUT, "facts.json"), "w", encoding="utf-8") as fh:
    json.dump(facts, fh, indent=2, default=str)

print("\n================ FACTS ================")
for k, v in facts.items():
    print(f"{k}: {v}")
