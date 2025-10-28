# Security Policy

## Supported Versions

We currently provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

Please do **NOT** report security vulnerabilities through public GitHub issues.

Instead, please report them via email to [security@python-practice.dev](mailto:security@python-practice.dev).

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information in your report:

- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to Expect

After you submit a report, we will:

1. Confirm receipt of your vulnerability report within 48 hours
2. Provide regular updates on our progress
3. Credit you in our security advisories (unless you prefer to remain anonymous)

### Security Best Practices

When using this project, please follow these security best practices:

1. **Keep dependencies updated**: Regularly update all dependencies to their latest secure versions
2. **Use virtual environments**: Always use virtual environments to isolate project dependencies
3. **Validate input**: Always validate and sanitize user input before processing
4. **Use HTTPS**: When making API calls, always use HTTPS endpoints
5. **Handle errors gracefully**: Don't expose sensitive information in error messages
6. **Review code**: Before using any code in production, review it for security issues

### Security Considerations

This project contains educational code examples. Some considerations:

- **Input validation**: Many examples may not include comprehensive input validation
- **Error handling**: Error handling may be simplified for educational purposes
- **Security features**: Security features may not be implemented in all examples
- **Production use**: Code should be reviewed and hardened before production use

### Dependencies

We regularly review and update our dependencies for security issues. You can check for known vulnerabilities using:

```bash
pip install safety
safety check
```

### Reporting Security Issues in Dependencies

If you discover a security issue in one of our dependencies:

1. Check if there's an updated version available
2. If not, report it to the dependency maintainers
3. Consider creating a pull request with a fix or workaround

## Security Updates

Security updates will be released as patch versions (e.g., 1.0.1, 1.0.2) and will be clearly marked in the changelog.

## Contact

For security-related questions or concerns, please contact us at [security@python-practice.dev](mailto:security@python-practice.dev).