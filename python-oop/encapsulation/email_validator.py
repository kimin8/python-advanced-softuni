class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        name, tokens = email.split("@")
        mail, domain = tokens.split(".")

        return (EmailValidator.__is_name_valid(self, name)
                and EmailValidator.__is_mail_valid(self, mail)
                and EmailValidator.__is_domain_valid(self, domain))
