from sklearn import tree

# Rough == 1
# Smooth == 0

# Cricket == 2
# Tennis == 1

def Ball_Dataset(weight, surface):
    
    BallsFeautures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(BallsFeautures, Names)

    result = clf.predict([[weight, surface]])

    if result == 1:
        print("Your object looks like Tennis Ball")
    elif result == 2:
        print("Your object looks like Cricket Ball")

def main():
    print("------- Welcome To Our Application ----------")

    print("Enter the weight of object")
    weight = input()

    print("What is the surface type of your object Rough or Smooth")
    surface = input()

    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Error : wrong input")
        exit()

    Ball_Dataset(weight,surface)

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()