class Solution:
    def reformatDate(self, date: str) -> str:
        mon=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        y=date[-4:]
        m=date[-8:-5]
        if m in mon:
            mn=mon.index(m)+1
        mn=str(mn)
        if len(mn)==1:
            mn="0"+mn
        d=date[:-11]
        if len(d)==1:
            d="0"+d
        return f"{y}-{mn}-{d}"