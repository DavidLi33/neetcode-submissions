class BrowserHistory:
    def __init__(self, homepage: str):
        self.page_index = 0
        self.len = 1
        self.history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.history) <= self.page_index + 1:
            self.history.append(url)
        else:
            self.history[self.page_index + 1] = url
        self.page_index += 1
        self.len = self.page_index+1

    def back(self, steps: int) -> str:
        self.page_index = max(self.page_index - steps, 0)
        return self.history[self.page_index]

    def forward(self, steps: int) -> str:
        self.page_index = min(self.page_index + steps, self.len-1)
        return self.history[self.page_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)