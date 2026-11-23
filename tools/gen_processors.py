"""Writes the fortress's processor list from YUNG's Better Nether Fortresses' own, with its Java
processors as processor data.

usage: python3 tools/gen_processors.py <YUNGs-Better-Fortresses>/Common/src/main/resources/data/betterfortresses

In the original's order: stair supports, nether wart, red sandstone stairs, the four pillar kinds
(with their altitude conditions), lava, then the vanilla rules as they are. The bridge arch
processor's markers become nether bricks; the arch it builds above them and the item frame
processor (it dresses entities) are left out.
"""
import json, os, sys

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'betterfortresses',
                   'worldgen', 'processor_list', 'main.json')


def state(s):
    """The 26.3 block state form: `id` and `properties`."""
    out = {'id': s['Name']}
    if s.get('Properties'):
        out['properties'] = s['Properties']
    return out


def randomizer(r):
    entries = []
    for e in r['entries']:
        entry = {'blockState': state(e['blockState']), 'probability': e['probability']}
        if 'condition' in e:
            entry['condition'] = e['condition']
        entries.append(entry)
    return {'entries': entries, 'defaultBlockState': state(r['defaultBlockState'])}


def translate(p):
    kind = p['processor_type']
    if kind == 'minecraft:rule':
        return [p]
    name = kind.split(':')[1]
    if name == 'stair_pillar_processor':
        # StairPillarProcessor: stone brick stairs become red nether brick stairs and purpur
        # stairs red nether bricks, each with a stair and a column under the block in front.
        return [{'processor_type': 'sunrise:stair_pillar',
                 'blocks': {'minecraft:stone_brick_stairs': 'minecraft:red_nether_brick_stairs',
                            'minecraft:purpur_stairs': 'minecraft:red_nether_bricks'},
                 'front': 'minecraft:red_nether_brick_stairs', 'pillar': 'minecraft:red_nether_bricks'}]
    if name == 'item_frame_processor':
        return []
    if name == 'bridge_arch_processor':
        return [{'processor_type': 'sunrise:pick', 'block': b, 'picks': [], 'default': {'state': {'id': 'minecraft:nether_bricks'}}}
                for b in ('minecraft:prismarine_stairs', 'minecraft:prismarine_brick_stairs')]
    if name == 'nether_wart_processor':
        # NetherWartProcessor: one wart in ten is missing.
        return [{'processor_type': 'sunrise:pick', 'block': 'minecraft:nether_wart',
                 'picks': [{'below': 0.1, 'state': {'id': 'minecraft:air'}}]}]
    if name == 'red_sandstone_stairs_processor':
        # RedSandstoneStairsProcessor: nether brick stairs with a nether brick column under them.
        return [{'processor_type': 'sunrise:yung_pillar', 'target_block': {'id': 'minecraft:red_sandstone_stairs'},
                 'target_block_output': {'entries': [], 'defaultBlockState': {'id': 'minecraft:nether_brick_stairs'}},
                 'pillar_states': {'entries': [], 'defaultBlockState': {'id': 'minecraft:nether_bricks'}},
                 'keep_properties': True}]
    if name == 'pillar_processor':
        return [{'processor_type': 'sunrise:yung_pillar', 'target_block': state(p['target_block']),
                 'target_block_output': randomizer(p['target_block_output']),
                 'pillar_states': randomizer(p['pillar_states'])}]
    if name == 'liquid_block_processor':
        return [{'processor_type': 'sunrise:pick', 'block': p['target_block']['Name'], 'picks': [],
                 'default': {'state': state(p['target_block_output'])}}]
    raise KeyError(kind)


def main():
    upstream = json.load(open(os.path.join(SRC, 'worldgen/processor_list/main.json')))
    ours = json.load(open(OUT))
    rules = [p for p in ours['processors'] if p['processor_type'] == 'minecraft:rule']
    out = []
    for p in upstream['processors']:
        if p['processor_type'] == 'minecraft:rule':
            out.append(rules.pop(0))
        else:
            out.extend(translate(p))
    assert not rules
    with open(OUT, 'w') as f:
        json.dump({'processors': out}, f, indent=2)
        f.write('\n')


if __name__ == '__main__':
    main()
