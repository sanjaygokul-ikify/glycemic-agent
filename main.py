import argparse
import json
from src.core import GlycemicAgent

def main():
    parser = argparse.ArgumentParser(description='Glycemic Agent')
    parser.add_argument('--config', type=str, default='config.json')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.load(f)
    agent = GlycemicAgent(config)
    agent.run()
if __name__ == '__main__':
    main()