from ml_models import run_regression
from clustering import run_clustering
from nlp_module import analyze_resume

def main():
    print("AI Career Recommendation System")
    print("--------------------------------")

    run_regression()
    run_clustering()

    resume = input("\nEnter resume text: ")
    career = analyze_resume(resume)
    print("Recommended Career:", career)

if __name__ == "__main__":
    main()
