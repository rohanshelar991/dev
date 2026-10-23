import unittest
from pathlib import Path

class LoginPageTests(unittest.TestCase):
    def test_login_page_exists(self):
        page = Path("app/index.html")
        self.assertTrue(page.exists())

    def test_login_page_contains_required_elements(self):
        content = Path("app/index.html").read_text()
        self.assertIn("Login Demo", content)
        self.assertIn('type="email"', content)
        self.assertIn('type="password"', content)
        self.assertIn("loginForm", content)

if __name__ == "__main__":
    unittest.main()
