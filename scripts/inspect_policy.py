from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import agent  # noqa: E402


def main() -> None:
    melon, wheat, carrot = agent._opening_maps(10)
    strawberries, melons, feed_wheat, flex = agent._long_term_site_sets(10)

    print("Kaggriculture policy inspection")
    print("================================")
    print(f"Opening: melon={len(melon)}, wheat={len(wheat)}, carrot={len(carrot)}")
    print(f"Long-term crop roles: strawberry={len(strawberries)}, melon={len(melons)}, feed_wheat={len(feed_wheat)}, flex={len(flex)}")
    print(f"Animal sites: {len(agent.ANIMAL_SITES)}")
    print("\nMarket-price snapshots around equilibrium inventory:")
    for item, params in agent.BASE_MARKET_PARAMS.items():
        i0 = params["I0"]
        low = agent._market_price(item, i0 - 100, {})
        mid = agent._market_price(item, i0, {})
        high = agent._market_price(item, i0 + 100, {})
        print(f"  {item:10s}: inventory {i0-100}/{i0}/{i0+100} -> price {low}/{mid}/{high}")


if __name__ == "__main__":
    main()
