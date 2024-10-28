#!/usr/bin/env python3

import argparse
import zxcvbn

def check_password_strength(password, verbose=False):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    strength_labels = ['Very Weak', 'Weak', 'Fair', 'Strong', 'Very Strong']
    
    print(f"Password strength: {strength_labels[score]} ({score}/4)")
    
    if feedback['warning']:
        print(f"Warning: {feedback['warning']}")
    
    if feedback['suggestions']:
        print("Suggestions:")
        for suggestion in feedback['suggestions']:
            print(f"- {suggestion}")

    if verbose:
        print("\nDetailed Information:")
        print(f"Guesses: {result['guesses']}")
        print(f"Guesses log10: {result['guesses_log10']:.1f}")
        
        print("\nCrack time estimates:")
        for scenario, seconds in result['crack_times_seconds'].items():
            readable = result['crack_times_display'][scenario]
            print(f"  {scenario}: {seconds:.2f} seconds ({readable})")
        
        if result['sequence']:
            print("\nIdentified patterns:")
            for pattern in result['sequence']:
                print(f"  - {pattern['pattern']} ({pattern['token']})")

def main():
    parser = argparse.ArgumentParser(
        description="Check password strength using the zxcvbn library.",
        usage="pwstrength.py [-h | --help] [-p | --password] [-v | --verbose]",
        epilog="""
Examples:
  pwstrength.py -p 'MyP@ssw0rd'
  pwstrength.py --password 'MyP@ssw0rd' -v

Note: For security reasons, avoid entering sensitive passwords directly in the command line.
Consider using this tool for testing or educational purposes only.
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-p", "--password", 
                        help="The password to check. Required.", 
                        required=True)
    parser.add_argument("-v", "--verbose", 
                        action="store_true", 
                        help="Enable verbose output. Provides detailed information including crack time estimates and identified patterns.")
    args = parser.parse_args()

    check_password_strength(args.password, args.verbose)
    
    print("\nUse 'history -d $((HISTCMD-1))' to remove the previous command from your shell history.")

if __name__ == "__main__":
    main()
