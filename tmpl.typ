#set page(
  paper: "a4",
)
#set text(
  size: 24pt,
)

#let today = datetime.today().display("[year]-[month]-[day]")

#set align(center)
#title(
  today + "算数题",
)
#block()

#set align(left)

#let formula_re = regex("^\$.+?\$$")
#let ans(show_ans: bool, body: str) = {
  set text(
    fill: green,
  )

  let s = {
    if body.match(formula_re) != none {
      eval(body)
    } else {
      body
    }
  }

  if show_ans {
    underline(s)
  } else {
    hide(s)
  }
}

#let show_ans = true
#let show_ans = sys.inputs.at("show_ans", default: "false") != "false"

#let data = csv("data.csv")

#grid(
  columns: 2,
  row-gutter: 5%,
  column-gutter: 20%,
  ..data.map(((q, a)) => {
    q
    ans(show_ans: show_ans, body: a)
    "\n"
  })
)
