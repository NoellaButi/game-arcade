# robot_builder.py
import random
import json
import textwrap

PARTS = {
    "Head": [("Basic Head", 50, {"vision": 1}), ("AI Head", 120, {"vision": 3})],
    "Torso": [("Light Torso", 70, {"defense": 1}), ("Armor Torso", 150, {"defense": 3})],
    "Arms": [("Clamp Arms", 40, {"power": 1}), ("Hydraulic Arms", 110, {"power": 3})],
    "Legs": [("Wheels", 60, {"speed": 2}), ("Biped Legs", 130, {"speed": 3})],
}
STAT_KEYS = ("vision", "defense", "power", "speed")


def _fmt_attr(attr: dict) -> str:
    return ", ".join(f"+{k} {v}" for k, v in attr.items())


def _sum_stats(chosen: dict) -> dict:
    totals = {k: 0 for k in STAT_KEYS}
    for _, (_, _, attr) in chosen.items():
        for k, v in attr.items():
            totals[k] = totals.get(k, 0) + v
    return totals


def robot_svg(parts: dict) -> str:
    """Return an SVG string previewing the selected parts."""
    head = parts.get("Head", "Basic Head")
    torso = parts.get("Torso", "Light Torso")
    arms = parts.get("Arms", "Clamp Arms")
    legs = parts.get("Legs", "Wheels")

    bg = "#0b1020"
    steel = "#9aa4b2"
    steel_dark = "#7d8794"
    pink = "#ff4b8b"
    mint = "#5eead4"
    gold = "#ffd166"
    tire = "#222"
    eye = "#f8fafc"

    torso_fill = pink if "Armor" in torso else "#5865f2"
    head_fill = "#3b82f6" if "Basic" in head else mint
    eye_w = 12 if "Basic" in head else 14
    antenna = "AI" in head
    arm_width = 10 if "Clamp" in arms else 16
    claw = "Clamp" in arms
    wheels = "Wheels" in legs

    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 420" width="100%" height="100%" style="background:{bg};border-radius:16px">
      <defs>
        <filter id="s" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#00000088"/>
        </filter>
      </defs>

      <ellipse cx="160" cy="400" rx="90" ry="12" fill="#00000055"/>

      <g filter="url(#s)">
        <rect x="110" y="160" width="100" height="120" rx="{18 if 'Armor' in torso else 28}"
              fill="{torso_fill}" stroke="#ffffff22" stroke-width="2"/>
        {"".join(f'<rect x="{120+i*20}" y="190" width="12" height="60" rx="3" fill="#ffffff20"/>' for i in (0,1,2,3))}
        {"".join(f'<circle cx="{135+i*25}" cy="180" r="4" fill="{c}"/>' for i,c in enumerate(("{gold}", "{mint}", "#60a5fa")))}
      </g>

      <g filter="url(#s)">
        <rect x="120" y="100" width="80" height="50" rx="12" fill="{head_fill}" />
        {"<line x1='160' y1='80' x2='160' y2='100' stroke='"+mint+"' stroke-width='3' />"
          "<circle cx='160' cy='78' r='4' fill='"+gold+"'/>" if antenna else ""}
        <rect x="135" y="118" width="{eye_w}" height="10" rx="5" fill="{eye}"/>
        <rect x="{175-eye_w}" y="118" width="{eye_w}" height="10" rx="5" fill="{eye}"/>
        <rect x="140" y="136" width="40" height="6" rx="3" fill="#0f172a" opacity="0.8"/>
      </g>

      <g stroke="{steel_dark}" stroke-width="2" fill="{steel}">
        <rect x="95" y="180" width="15" height="70" rx="6"/>
        <rect x="{95 - arm_width}" y="235" width="{arm_width}" height="12" rx="6"/>
        {"<polygon points='85,241 75,236 75,246' fill='"+steel+"'/>" if claw else
          "<rect x='76' y='235' width='12' height='12' rx='2'/>"}
        <rect x="210" y="180" width="15" height="70" rx="6"/>
        <rect x="225" y="235" width="{arm_width}" height="12" rx="6"/>
        {"<polygon points='245,241 255,236 255,246' fill='"+steel+"'/>" if claw else
          "<rect x='232' y='235' width='12' height='12' rx='2'/>"}
      </g>

      <rect x="135" y="280" width="50" height="10" rx="5" fill="{steel_dark}"/>

      {"".join([
        f"<g><rect x='140' y='290' width='40' height='10' rx='5' fill='{steel_dark}'/>"
        f"<circle cx='155' cy='330' r='18' fill='{tire}' stroke='#555' stroke-width='2'/>"
        f"<circle cx='165' cy='330' r='18' fill='{tire}' stroke='#555' stroke-width='2'/>"
        f"<circle cx='155' cy='330' r='6' fill='{steel}'/><circle cx='165' cy='330' r='6' fill='{steel}'/></g>"
      ]) if wheels else
      "".join([
        f"<g stroke='{steel_dark}' stroke-width='2'>"
        f"<rect x='145' y='290' width='10' height='50' rx='4' fill='{steel}'/>"
        f"<rect x='165' y='290' width='10' height='50' rx='4' fill='{steel}'/>"
        f"<rect x='135' y='338' width='30' height='8' rx='3' fill='{steel_dark}'/>"
        f"<rect x='165' y='338' width='30' height='8' rx='3' fill='{steel_dark}'/></g>"
      ])}

      <text x="160" y="30" text-anchor="middle" fill="#cbd5e1" font-family="monospace" font-size="14">Robot Preview</text>
    </svg>
    """
    return textwrap.dedent(svg)


def _build_dict(chosen, budget, cost, totals):
    return {
        "budget": budget,
        "cost": cost,
        "parts": {slot: name for slot, (name, _, _) in chosen.items()},
        "stats": totals,
    }


def render_st(st):
    st.header("🤖 Robot Builder")

    if "rb_budget" not in st.session_state:
        st.session_state.rb_budget = 300
        st.session_state.rb_picks = {slot: 0 for slot in PARTS.keys()}

    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        st.session_state.rb_budget = st.number_input(
            "Budget ($)", 100, 1000, st.session_state.rb_budget, 10
        )

    with col_b:
        if st.button("Randomize (fit budget)"):
            for _ in range(200):
                picks = {slot: random.randrange(len(opts)) for slot, opts in PARTS.items()}
                cost_try = sum(PARTS[s][i][1] for s, i in picks.items())
                if cost_try <= st.session_state.rb_budget:
                    st.session_state.rb_picks = picks
                    break
            else:
                st.session_state.rb_picks = {
                    s: min(range(len(opts)), key=lambda i: opts[i][1]) for s, opts in PARTS.items()
                }

    with col_c:
        if st.button("Reset"):
            st.session_state.rb_budget = 300
            st.session_state.rb_picks = {slot: 0 for slot in PARTS.keys()}
            st.rerun()

    st.write("---")

    chosen = {}
    total_cost = 0

    for slot, options in PARTS.items():
        labels = [f"{name} — ${price} ({_fmt_attr(attr)})" for name, price, attr in options]
        idx = st.selectbox(
            f"{slot}:",
            options=list(range(len(labels))),
            format_func=lambda i, L=labels: L[i],
            index=st.session_state.rb_picks[slot],
            key=f"rb_{slot}",
        )
        st.session_state.rb_picks[slot] = idx
        choice = options[idx]
        chosen[slot] = choice
        total_cost += choice[1]

    totals = _sum_stats(chosen)

    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.metric("💵 Cost", f"${total_cost}")
    with m2:
        st.metric("🎯 Budget", f"${st.session_state.rb_budget}")
    with m3:
        st.metric("👁 Vision", totals.get("vision", 0))
    with m4:
        st.metric("🛡 Defense", totals.get("defense", 0))
    with m5:
        st.metric("⚡ Power / 🏃 Speed", f"{totals.get('power', 0)} / {totals.get('speed', 0)}")

    st.progress(min(1.0, total_cost / max(1, st.session_state.rb_budget)))

    left, right = st.columns([1.1, 1])
    with left:
        parts_names = {slot: name for slot, (name, _, _) in chosen.items()}
        svg = robot_svg(parts_names)
        st.components.v1.html(svg, height=440, scrolling=False)

    with right:
        build = _build_dict(chosen, st.session_state.rb_budget, total_cost, totals)
        st.code(json.dumps(build["parts"], indent=2))
        if total_cost > st.session_state.rb_budget:
            st.error("Over budget! Pick cheaper parts.")
        else:
            st.success("Within budget — robot ready!")

        st.download_button(
            "💾 Save Build (JSON)",
            data=json.dumps(build, indent=2),
            file_name="robot_build.json",
            mime="application/json",
        )
