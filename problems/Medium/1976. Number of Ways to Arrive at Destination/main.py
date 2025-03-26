from typing import *
import heapq
from collections import defaultdict
MOD = 1_000_000_007
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # dijstra algorithms 
        if n == 1:
            return 1
        if n == 2:
            return 1
        graph = defaultdict(dict)
        mymap = {}
        for u,v,w in roads:
            graph[u][v] = w 
            graph[v][u] = w 
        for i in range(n):
            mymap[i] = {
                'count_path': 0,
                'min_distance': float('inf'),
            }
        mymap[0]['min_distance'] = 0
        mymap[0]['count_path'] = 1
        def bfs(start):
            cache = {}
            queue = [(0,start)]
            visited = set()
            while queue:
                _,node = heapq.heappop(queue)
                if node in visited:
                    continue
                visited.add(node)
                distance = mymap[node]['min_distance']
                for neighbor,weight in graph[node].items():
                    distance_neighbor = mymap[neighbor]['min_distance']
                    if distance + weight < distance_neighbor:
                        mymap[neighbor]['count_path'] = mymap[node]['count_path']
                        distance_neighbor = distance + weight
                    elif (distance + weight) == distance_neighbor:             
                        mymap[neighbor]['count_path'] += mymap[node]['count_path']
                    mymap[neighbor]['min_distance'] = distance_neighbor
                    if neighbor not in visited:
                        heapq.heappush(queue,(distance_neighbor,neighbor))
        bfs(0)
        r = mymap[n-1]['count_path'] % MOD
        return int(r)


                

                

        




if __name__ == '__main__':
    n =  43
    roads = [[1,0,8262],[2,0,8854],[3,2,1655],[0,3,10509],[4,0,239],[5,4,16047],[2,5,7432],[0,5,16286],[6,0,16895],[5,6,609],[6,1,8633],[6,2,8041],[6,4,16656],[7,4,26326],[5,7,10279],[7,6,9670],[8,6,12706],[0,8,29601],[7,8,3036],[8,2,20747],[8,1,21339],[4,9,26342],[9,0,26581],[2,9,17727],[9,1,18319],[9,7,16],[6,9,9686],[2,10,21006],[10,5,13574],[0,10,29860],[1,10,21598],[10,8,259],[10,6,12965],[10,3,19351],[8,11,917],[5,11,14232],[11,7,3953],[0,11,30518],[11,10,658],[4,11,30279],[11,2,21664],[9,11,3937],[1,11,22256],[6,11,13623],[12,1,9108],[6,12,475],[13,2,9310],[14,13,15234],[14,9,6817],[14,7,6833],[14,12,16028],[14,0,33398],[14,1,25136],[14,6,16503],[5,14,17112],[15,2,27346],[15,12,18830],[10,15,6340],[15,6,19305],[5,15,19914],[8,15,6599],[4,15,35961],[3,15,25691],[15,9,9619],[0,15,36200],[11,15,5682],[14,15,2802],[7,15,9635],[1,15,27938],[13,15,18036],[4,16,40527],[16,0,40766],[16,9,14185],[16,14,7368],[16,10,10906],[5,16,24480],[16,7,14201],[15,16,4566],[16,8,11165],[11,16,10248],[13,16,22602],[12,16,23396],[2,16,31912],[16,1,32504],[16,6,23871],[3,16,30257],[17,15,7284],[3,17,32975],[17,10,13624],[17,9,16903],[14,17,10086],[17,2,34630],[4,18,43207],[18,3,32937],[15,18,7246],[18,7,16881],[19,8,15714],[19,12,27945],[7,19,18750],[17,19,1831],[10,19,15455],[4,20,47453],[20,15,11492],[20,19,2377],[20,11,17174],[20,5,31406],[20,8,18091],[20,2,38838],[16,20,6926],[20,6,30797],[14,21,23681],[4,21,56840],[8,21,27478],[21,6,40184],[21,1,48817],[21,7,30514],[9,21,30498],[0,21,57079],[21,16,16313],[21,5,40793],[15,21,20879],[21,3,46570],[12,21,39709],[17,21,13595],[21,2,48225],[13,21,38915],[10,21,27219],[18,21,13633],[20,21,9387],[19,21,11764],[21,11,26561],[22,7,7281],[10,22,3986],[22,3,23337],[11,23,1665],[3,24,49706],[24,17,16731],[4,24,59976],[24,5,43929],[2,24,51361],[24,13,42051],[18,24,16769],[24,19,14900],[24,12,42845],[24,14,26817],[24,20,12523],[24,22,26369],[10,24,30355],[24,8,30614],[24,21,3136],[9,24,33634],[0,24,60215],[24,1,51953],[16,24,19449],[24,15,24015],[24,7,33650],[24,6,43320],[24,11,29697],[25,15,29658],[25,13,47694],[25,20,18166],[25,21,8779],[12,25,48488],[11,25,35340],[25,0,65858],[26,23,42976],[6,26,58264],[26,9,48578],[26,0,75159],[19,26,29844],[4,26,74920],[26,1,66897],[18,26,31713],[17,26,31675],[15,26,38959],[24,26,14944],[14,26,41761],[2,26,66305],[26,12,57789],[26,25,9301],[22,26,41313],[7,26,48594],[8,26,45558],[26,16,34393],[10,26,45299],[11,26,44641],[26,20,27467],[13,26,56995],[26,21,18080],[26,3,64650],[16,27,42083],[15,27,46649],[12,27,65479],[0,27,82849],[27,3,72340],[27,7,56284],[8,27,53248],[26,27,7690],[4,27,82610],[14,27,49451],[27,10,52989],[20,27,35157],[27,25,16991],[27,19,37534],[27,13,64685],[9,27,56268],[27,5,66563],[27,22,49003],[24,27,22634],[1,27,74587],[27,2,73995],[27,17,39365],[27,11,52331],[27,23,50666],[27,21,25770],[28,6,58907],[20,28,28110],[19,28,30487],[28,2,66948],[25,28,9944],[28,1,67540],[28,23,43619],[28,10,45942],[24,29,30552],[14,29,57369],[6,29,73872],[12,29,73397],[29,22,56921],[29,18,47321],[9,29,64186],[29,2,81913],[19,29,45452],[4,29,90528],[3,29,80258],[11,29,60249],[1,29,82505],[10,29,60907],[29,7,64202],[20,29,43075],[29,13,72603],[28,29,14965],[8,29,61166],[25,29,24909],[0,29,90767],[29,26,15608],[29,23,58584],[5,29,74481],[29,21,33688],[29,17,47283],[16,29,50001],[29,27,7918],[29,15,54567],[30,15,52577],[30,12,71407],[17,30,45293],[30,3,78268],[5,30,72491],[30,10,58917],[30,22,54931],[8,30,59176],[27,30,5928],[30,28,12975],[30,7,62212],[30,13,70613],[31,12,80098],[31,9,70887],[31,6,80573],[31,15,61268],[31,14,64070],[2,31,88614],[31,8,67867],[19,31,52153],[21,31,40389],[24,31,37253],[4,31,97229],[29,31,6701],[19,32,61065],[32,2,97526],[32,26,31221],[32,10,76520],[6,32,89485],[32,9,79799],[32,29,15613],[32,20,58688],[32,24,46165],[18,32,62934],[17,32,62896],[32,31,8912],[32,28,30578],[15,32,70180],[32,0,106380],[23,32,74197],[32,5,90094],[27,32,23531],[32,25,40522],[32,13,88216],[14,32,72982],[3,32,95871],[30,32,17603],[32,16,65614],[1,32,98118],[11,32,75862],[21,32,49301],[6,33,94770],[29,33,20898],[33,13,93501],[21,33,54586],[33,32,5285],[5,33,95379],[33,9,85084],[33,8,82064],[33,26,36506],[17,33,68181],[33,7,85100],[14,33,78267],[33,20,63973],[23,33,79482],[33,16,70899],[33,0,111665],[25,33,45807],[22,33,77819],[30,33,22888],[33,27,28816],[33,31,14197],[33,19,66350],[33,10,81805],[2,33,102811],[34,2,105016],[34,3,103361],[27,34,31021],[34,10,84010],[8,34,84269],[34,9,87289],[33,34,2205],[18,34,70424],[34,4,113631],[19,34,68555],[34,25,48012],[34,31,16402],[5,34,97584],[7,34,87305],[34,17,70386],[34,28,38068],[16,34,73104],[34,30,25093],[24,34,53655],[34,11,83352],[15,34,77670],[32,34,7490],[21,34,56791],[14,34,80472],[23,34,81687],[12,34,96500],[26,34,38711],[34,13,95706],[34,29,23103],[34,22,80024],[35,14,80483],[5,35,97595],[35,2,105027],[17,35,70397],[35,1,105619],[35,23,81698],[12,35,96511],[35,25,48023],[35,33,2216],[35,30,25104],[3,35,103372],[22,35,80035],[13,35,95717],[26,35,38722],[35,10,84021],[4,35,113642],[18,35,70435],[32,35,7501],[11,35,83363],[35,9,87300],[35,19,68566],[21,35,56802],[35,7,87316],[35,20,66189],[35,27,31032],[35,15,77681],[24,35,53666],[35,28,38079],[29,35,23114],[8,35,84280],[0,35,113881],[31,35,16413],[16,35,73115],[35,34,11],[6,35,96986],[36,18,73807],[17,36,73769],[36,12,99883],[31,36,19785],[6,36,100358],[1,36,108991],[30,36,28476],[3,36,106744],[36,7,90688],[36,25,51395],[36,28,41451],[11,36,86735],[10,36,87393],[36,29,26486],[34,36,3383],[21,36,60174],[36,33,5588],[35,36,3372],[4,36,117014],[15,36,81053],[36,22,83407],[26,36,42094],[36,2,108399],[37,35,11770],[37,24,65436],[36,37,8398],[37,9,99070],[25,37,59793],[37,28,49849],[37,1,117389],[37,0,125651],[37,19,80336],[37,10,95791],[37,27,42802],[14,37,92253],[37,7,99086],[37,8,96050],[37,15,89451],[37,11,95133],[37,5,109365],[20,37,77959],[37,2,116797],[6,37,108756],[37,3,115142],[37,33,13986],[37,21,68572],[22,37,91805],[17,37,82167],[18,37,82205],[12,37,108281],[37,32,19271],[13,37,107487],[16,37,84885],[37,4,125412],[31,37,28183],[34,37,11781],[29,37,34884],[30,37,36874],[38,0,132072],[38,36,14819],[34,38,18202],[38,2,123218],[38,12,114702],[38,11,101554],[38,31,34604],[1,38,123810],[13,38,113908],[38,9,105491],[32,38,25692],[18,38,88626],[38,19,86757],[16,38,91306],[3,38,121563],[17,38,88588],[38,15,95872],[7,38,105507],[38,20,84380],[38,5,115786],[37,38,6421],[38,24,71857],[38,4,131833],[38,28,56270],[38,25,66214],[6,38,115177],[38,33,20407],[26,38,56913],[38,22,98226],[39,28,13815],[39,22,55771],[39,14,56219],[20,39,41925],[39,13,71453],[39,27,6768],[40,34,17896],[16,40,91000],[40,20,84074],[40,10,101906],[24,40,71551],[40,36,14513],[29,40,40999],[40,7,105201],[40,9,105185],[18,40,88320],[35,40,17885],[12,40,114396],[33,40,20101],[39,40,42149],[40,6,114871],[5,40,115480],[40,32,25386],[40,23,99583],[13,40,113602],[40,4,131527],[11,40,101248],[8,40,102165],[14,40,98368],[40,27,48917],[31,40,34298],[17,40,88282],[1,40,123504],[40,15,95566],[28,40,55964],[37,40,6115],[0,40,131766],[40,21,74687],[26,40,56607],[41,33,21774],[23,41,101256],[41,14,100041],[25,41,67581],[41,12,116069],[41,20,85747],[41,17,89955],[28,41,57637],[3,41,122930],[40,41,1673],[15,41,97239],[41,10,103579],[5,41,117153],[26,41,58280],[41,7,106874],[38,41,1367],[41,32,27059],[36,41,16186],[41,37,7788],[41,24,73224],[18,41,89993],[41,13,115275],[41,30,44662],[41,39,43822],[8,41,103838],[19,41,88124],[21,41,76360],[2,41,124585],[4,41,133200],[41,34,19569],[41,31,35971],[6,41,116544],[41,9,106858],[41,22,99593],[41,35,19558],[0,41,133439],[29,41,42672],[41,16,92673],[41,11,102921],[42,36,23840],[7,42,114528],[42,13,122929],[42,6,124198],[42,39,51476],[0,42,141093],[42,31,43625],[42,34,27223],[22,42,107247],[42,23,108910],[42,35,27212],[4,42,140854],[42,38,9021],[3,42,130584],[42,2,132239],[24,42,80878],[16,42,100327],[11,42,110575],[9,42,114512],[42,5,124807],[33,42,29428],[10,42,111233],[42,25,75235],[42,28,65291],[12,42,123723],[8,42,111492],[32,42,34713],[42,21,84014],[42,17,97609],[42,37,15442],[19,42,95778],[42,30,52316],[20,42,93401],[41,42,7654],[42,40,9327],[15,42,104893],[42,26,65934],[42,29,50326],[42,18,97647]]
    # n = 7
    # roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    n = 47
    roads = [[1,0,3233],[1,2,5575],[2,0,8808],[3,1,3576],[0,3,6809],[4,2,8393],[0,4,17201],[5,2,9453],[5,0,18261],[5,4,1060],[5,3,11452],[6,3,20051],[6,2,18052],[5,6,8599],[6,0,26860],[4,6,9659],[1,6,23627],[3,7,3440],[8,4,10812],[2,8,19205],[5,8,9752],[1,8,24780],[8,7,17764],[6,8,1153],[8,3,21204],[8,0,28013],[9,6,5862],[7,9,22473],[9,2,23914],[9,4,15521],[9,8,4709],[1,9,29489],[5,9,14461],[0,9,32722],[9,3,25913],[10,3,4235],[10,2,2236],[0,10,11044],[11,10,23371],[1,11,31182],[11,3,27606],[6,11,7555],[11,9,1693],[2,11,25607],[8,11,6402],[11,0,34415],[11,4,17214],[7,11,24166],[5,11,16154],[6,12,15767],[12,9,9905],[4,12,25426],[0,12,42627],[12,5,24366],[12,3,35818],[12,8,14614],[12,10,31583],[12,11,8212],[7,12,32378],[12,1,39394],[2,12,33819],[2,13,40532],[8,13,21327],[13,1,46107],[13,12,6713],[3,13,42531],[11,13,14925],[14,8,3362],[1,14,28142],[15,14,6053],[8,16,28951],[16,10,45920],[14,16,25589],[5,16,38703],[16,2,48156],[13,16,7624],[16,15,19536],[16,6,30104],[16,1,53731],[16,3,50155],[9,16,24242],[16,4,39763],[12,16,14337],[14,17,19219],[0,17,50594],[7,17,40345],[17,12,7967],[17,5,32333],[17,9,17872],[1,17,47361],[13,17,1254],[18,17,6103],[18,1,53464],[18,12,14070],[18,8,28684],[11,18,22282],[18,6,29837],[18,7,46448],[10,18,45653],[4,18,39496],[18,9,23975],[3,18,49888],[18,15,19269],[19,16,1549],[19,12,15886],[19,13,9173],[7,19,48264],[19,2,49705],[19,11,24098],[3,19,51704],[4,19,41312],[19,1,55280],[9,19,25791],[15,19,21085],[19,0,58513],[17,19,7919],[9,20,25990],[12,20,16085],[15,20,21284],[0,20,58712],[1,20,55479],[11,20,24297],[4,20,41511],[20,14,27337],[20,2,49904],[20,10,47668],[20,17,8118],[20,3,51903],[16,20,1748],[8,20,30699],[20,13,9372],[5,20,40451],[19,20,199],[20,18,2015],[21,9,10192],[21,5,24653],[3,21,36105],[21,12,287],[4,21,25713],[22,19,801],[21,22,16400],[13,22,9974],[22,1,56081],[22,0,59314],[3,22,52505],[22,20,602],[22,14,27939],[9,22,26592],[4,22,42113],[22,10,48270],[22,7,49065],[22,15,21886],[22,2,50506],[18,22,2617],[11,22,24899],[22,12,16687],[22,17,8720],[22,6,32454],[16,22,2350],[22,23,2765],[11,23,27664],[23,17,11485],[23,20,3367],[3,23,55270],[23,1,58846],[12,23,19452],[23,13,12739],[23,4,44878],[0,23,62079],[6,23,35219],[19,23,3566],[23,8,34066],[23,18,5382],[5,23,43818],[23,9,29357],[10,23,51035],[2,23,53271],[23,21,19165],[23,15,24651],[23,14,30704],[7,23,51830],[24,22,12265],[10,24,60535],[24,4,54378],[24,5,53318],[3,24,64770],[0,24,71579],[24,11,37164],[6,24,44719],[14,24,40204],[1,24,68346],[20,24,12867],[7,24,61330],[24,19,13066],[24,23,9500],[13,24,22239],[17,24,20985],[24,9,38857],[11,25,28058],[14,25,31098],[9,25,29751],[25,12,19846],[4,25,45272],[25,23,394],[25,5,44212],[8,25,34460],[25,2,53665],[25,17,11879],[25,16,5509],[10,25,51429],[15,26,37981],[26,21,32495],[26,23,13330],[24,26,3830],[4,26,58208],[0,26,75409],[10,26,64365],[26,3,68600],[26,11,40994],[26,2,66601],[6,26,48549],[13,26,26069],[0,27,82747],[7,27,72498],[27,2,73939],[27,26,7338],[27,15,45319],[27,23,20668],[21,27,39833],[3,27,75938],[27,16,25783],[9,27,50025],[27,1,79514],[27,20,24035],[10,27,71703],[27,6,55887],[5,27,64486],[25,27,20274],[18,27,26050],[27,8,54734],[27,4,65546],[27,12,40120],[24,28,7405],[28,12,36357],[28,0,78984],[28,10,67940],[14,28,47609],[7,28,68735],[8,29,54915],[29,26,7519],[15,29,45500],[29,4,65727],[2,29,74120],[29,5,64667],[1,29,79695],[25,29,20455],[0,29,82928],[21,29,40014],[3,29,76119],[29,23,20849],[12,29,40301],[28,29,3944],[29,17,32334],[19,29,24415],[14,29,51553],[22,29,23614],[29,10,71884],[29,11,48513],[29,24,11349],[29,7,72679],[29,27,181],[29,6,56068],[29,20,24216],[29,16,25964],[30,8,58234],[30,22,26933],[27,30,3500],[4,30,69046],[30,9,53525],[30,3,79438],[30,10,75203],[30,29,3319],[28,30,7263],[14,30,54872],[30,20,27535],[30,25,23774],[30,2,77439],[30,23,24168],[30,5,67986],[21,30,43333],[30,16,29283],[0,30,86247],[15,30,48819],[30,19,27734],[30,13,36907],[7,30,75998],[30,12,43620],[1,30,83014],[30,24,14668],[18,30,29550],[9,31,59524],[31,20,33534],[31,10,81202],[31,25,29773],[1,31,89013],[31,24,20667],[30,31,5999],[18,31,35549],[31,13,42906],[2,31,83438],[31,29,9318],[31,26,16837],[22,31,32932],[4,31,75045],[31,7,81997],[14,31,60871],[31,8,64233],[11,31,57831],[31,23,30167],[31,27,9499],[29,32,11204],[15,32,56704],[25,32,31659],[32,4,76931],[17,32,43538],[13,32,44792],[32,12,51505],[32,27,11385],[21,32,51218],[32,22,34818],[32,30,7885],[33,6,58334],[33,0,85194],[22,33,25880],[33,7,74945],[33,9,52472],[33,24,13615],[33,26,9785],[33,19,26681],[33,8,57181],[34,13,46224],[34,15,58136],[34,1,92331],[8,34,67551],[34,17,44970],[34,25,33091],[34,32,1432],[5,34,77303],[4,34,78363],[20,34,36852],[34,31,3318],[34,19,37051],[34,0,95564],[34,2,86756],[34,23,33485],[27,34,12817],[34,9,62842],[34,18,38867],[34,33,10370],[34,24,23985],[34,10,84520],[6,34,68704],[34,7,85315],[28,34,16580],[34,29,12636],[14,34,64189],[3,34,88755],[34,30,9317],[34,21,52650],[34,16,38600],[11,34,61149],[35,29,20510],[22,35,44124],[19,35,44925],[17,35,52844],[35,5,85177],[13,35,54098],[35,2,94630],[21,35,60524],[4,35,86237],[35,10,92394],[9,35,70716],[35,20,44726],[12,35,60811],[14,35,72063],[35,26,28029],[35,8,75425],[35,28,24454],[35,16,46474],[35,3,96629],[35,34,7874],[35,0,103438],[35,15,66010],[35,6,76578],[24,35,31859],[25,35,40965],[35,27,20691],[3,36,106449],[5,36,94997],[11,36,78843],[36,29,30330],[26,36,37849],[36,9,80536],[12,36,70631],[0,36,113258],[34,36,17694],[36,21,70344],[31,36,21012],[36,10,102214],[6,36,86398],[36,4,96057],[36,24,41679],[36,30,27011],[1,36,110025],[36,35,9820],[36,16,56294],[17,36,62664],[8,36,85245],[36,15,75830],[36,28,34274],[13,36,63918],[36,18,56561],[36,14,81883],[37,34,25794],[20,37,62646],[12,37,78731],[7,37,111109],[8,37,93345],[2,37,112550],[4,37,104157],[27,37,38611],[37,22,62044],[28,37,42374],[35,37,17920],[37,5,103097],[23,37,59279],[37,19,62845],[37,10,110314],[37,36,8100],[37,17,70764],[37,6,94498],[37,26,45949],[37,11,86943],[37,31,29112],[33,37,36164],[37,32,27226],[37,25,58885],[29,37,38430],[3,37,114549],[37,18,64661],[37,15,83930],[37,38,2541],[10,38,112855],[39,22,72121],[39,18,74738],[39,19,72922],[7,39,121186],[39,23,69356],[39,26,56026],[39,34,35871],[35,39,27997],[36,39,18177],[1,39,128202],[15,39,94007],[21,39,88521],[38,39,7536],[39,33,46241],[6,39,104575],[31,39,39189],[39,9,98713],[20,39,72723],[27,39,48688],[29,39,48507],[16,39,74471],[11,39,97020],[24,39,59856],[39,8,103422],[39,14,100060],[39,10,120391],[39,5,113174],[39,32,37303],[39,2,122627],[25,39,68962],[39,13,82095],[3,39,124626],[2,40,129296],[36,40,24846],[24,40,66525],[40,18,81407],[40,13,88764],[25,40,75631],[40,29,55176],[40,17,87510],[40,21,95190],[9,40,105382],[40,6,111244],[34,40,42540],[26,40,62695],[19,40,79591],[39,40,6669],[40,33,52910],[40,27,55357],[29,41,49530],[41,39,1023],[7,41,122209],[41,20,73746],[26,41,57049],[25,41,69985],[41,13,83118],[19,41,73945],[32,41,38326],[31,41,40212],[11,41,98043],[41,35,29020],[41,14,101083],[41,2,123650],[41,0,132458],[41,5,114197],[18,41,75761],[41,6,105598],[38,41,8559],[41,21,89544],[41,3,125649],[41,33,47264],[28,41,53474],[41,12,89831],[41,24,60879],[15,41,95030],[36,41,19200],[41,1,129225],[42,14,110641],[16,42,85052],[42,4,124815],[42,13,92676],[42,18,85319],[40,42,3912],[42,30,55769],[42,34,46452],[39,42,10581],[42,2,133208],[15,42,104588],[42,33,56822],[37,42,20658],[20,42,83304],[42,11,107601],[3,42,135207],[25,42,79543],[42,32,47884],[42,29,59088],[36,42,28758],[31,42,49770],[42,1,138783],[42,23,79937],[28,42,63032],[12,42,99389],[42,21,99102],[42,38,18117],[42,22,82702],[0,42,142016],[27,42,59269],[42,17,91422],[42,35,38578],[42,8,114003],[42,7,131767],[42,5,123755],[43,42,9318],[30,43,65087],[41,43,18876],[43,20,92622],[40,43,13230],[14,43,119959],[43,29,68406],[25,43,88861],[34,43,55770],[43,27,68587],[37,43,29976],[31,44,64955],[42,44,15185],[27,44,74454],[17,44,106607],[44,40,19097],[6,44,130341],[44,35,53763],[44,22,97887],[44,21,114287],[44,33,72007],[36,44,43943],[3,44,150392],[44,0,157201],[44,5,138940],[12,44,114574],[44,23,95122],[10,44,146157],[18,44,100504],[44,2,148393],[16,44,100237],[11,44,122786],[43,44,5867],[44,41,24743],[44,26,81792],[30,44,70954],[24,44,85622],[44,37,35843],[9,44,124479],[44,20,98489],[44,1,153968],[44,34,61637],[44,39,25766],[44,19,98688],[7,44,146952],[44,28,78217],[25,44,94728],[44,13,107861],[15,44,119773],[32,44,63069],[29,44,74273],[14,44,125826],[44,8,129188],[44,45,2211],[45,17,108818],[45,38,35513],[45,8,131399],[30,45,73165],[45,34,63848],[45,2,150604],[45,5,141151],[28,45,80428],[45,37,38054],[1,45,156179],[35,45,55974],[45,24,87833],[29,45,76484],[45,14,128037],[45,20,100700],[3,45,152603],[45,31,67166],[45,10,148368],[45,36,46154],[43,45,8078],[11,45,124997],[16,45,102448],[25,45,96939],[45,40,21308],[32,45,65280],[45,15,121984],[7,45,149163],[26,45,84003],[45,13,110072],[0,45,159412],[6,45,132552],[45,33,74218],[46,20,103665],[33,46,77183],[46,16,105413],[38,46,38478],[19,46,103864],[46,17,111783],[46,2,153569],[41,46,29919],[46,9,129655],[46,39,30942],[40,46,24273],[26,46,86968],[46,11,127962],[30,46,76130],[44,46,5176],[10,46,151333],[46,34,66813],[46,6,135517],[46,18,105680],[1,46,159144],[25,46,99904],[46,43,11043],[29,46,79449],[46,8,134364],[42,46,20361]]
    roads = [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]]
    n = 6
    r = Solution().countPaths(n,roads)
    print(r)
    
