final_analysis <- read_csv("final_analysis.csv")

final_analysis <-arrange(final_analysis, final_analysis$bc, final_analysis$dc, final_analysis$cc, final_analysis$ec)
top20 = head(final_analysis,21)
library(igraph)
g = graph_from_data_frame(top20, directed = FALSE)
plot(g, vertex.size=10, vertex.label = top20$`Legislator name`,  vertex.size=top20$`Legislative Effectiveness Score`)