#!/bin/bash
# =============================================================================
# Script de Gestion des Branches - Formation Python 🐛
# =============================================================================

echo "🐛 GESTIONNAIRE DES BRANCHES FORMATION PYTHON"
echo "=============================================="

# Fonction pour afficher l'aide
show_help() {
    echo "Usage: ./manage_branches.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  --to-main       Basculer vers la branche main (pour les étudiants)"
    echo "  --to-solution   Basculer vers la branche solution (pour les formateurs)"
    echo "  --status        Afficher l'état des deux branches"
    echo "  --push-all      Pousser les deux branches sur le remote"
    echo "  --help          Afficher cette aide"
    echo ""
    echo "Description des branches:"
    echo "  📚 main     : Version étudiants (sans solutions)"
    echo "  🔑 solution : Version formateurs (avec solutions complètes)"
}

# Fonction pour basculer vers main
switch_to_main() {
    echo "📚 Basculement vers la branche MAIN (version étudiants)..."
    git checkout main
    
    if [ $? -eq 0 ]; then
        echo "✅ Vous êtes maintenant sur la branche MAIN"
        echo "📋 Cette branche contient :"
        echo "   - Les exercices et challenges"
        echo "   - Les fichiers markdown avec explications"
        echo "   - Pas de solutions complètes"
        echo ""
        echo "🚫 Dossiers ignorés (non visibles):"
        echo "   - Jour_05-06_POO/"
        echo "   - Jour_07-08_Fichiers_Erreurs/"
        echo "   - Jour_09-10_Projet_Final/"
    else
        echo "❌ Erreur lors du basculement vers main"
    fi
}

# Fonction pour basculer vers solution
switch_to_solution() {
    echo "🔑 Basculement vers la branche SOLUTION (version formateurs)..."
    git checkout solution
    
    if [ $? -eq 0 ]; then
        echo "✅ Vous êtes maintenant sur la branche SOLUTION"
        echo "📋 Cette branche contient :"
        echo "   - Tous les exercices et challenges"
        echo "   - Toutes les solutions complètes"
        echo "   - Les projets avancés"
        echo "   - La documentation complète"
        echo ""
        echo "📁 Dossiers disponibles:"
        echo "   - Jour_05-06_POO/ (Solutions POO complètes)"
        echo "   - Jour_07-08_Fichiers_Erreurs/ (Gestion fichiers/erreurs)"
        echo "   - Jour_09-10_Projet_Final/ (Projet école complet)"
    else
        echo "❌ Erreur lors du basculement vers solution"
    fi
}

# Fonction pour afficher le statut
show_status() {
    echo "📊 STATUT DES BRANCHES"
    echo "====================="
    
    current_branch=$(git branch --show-current)
    echo "🔹 Branche actuelle: $current_branch"
    echo ""
    
    echo "📚 Branche MAIN (étudiants):"
    git show main --name-only --format="" | head -10
    echo ""
    
    echo "🔑 Branche SOLUTION (formateurs):"
    git show solution --name-only --format="" | head -10
    echo ""
    
    echo "📈 Statistiques:"
    main_files=$(git ls-tree -r main | wc -l)
    solution_files=$(git ls-tree -r solution | wc -l)
    echo "   - Fichiers dans main: $main_files"
    echo "   - Fichiers dans solution: $solution_files"
    echo "   - Fichiers de solutions: $((solution_files - main_files))"
}

# Fonction pour pousser toutes les branches
push_all() {
    echo "🚀 PUSH DES DEUX BRANCHES"
    echo "========================"
    
    current_branch=$(git branch --show-current)
    
    echo "📤 Push de la branche main..."
    git push origin main
    
    echo "📤 Push de la branche solution..."
    git push origin solution
    
    # Retourner à la branche d'origine
    git checkout $current_branch
    
    echo "✅ Push terminé pour les deux branches"
}

# Traitement des arguments
case "$1" in
    --to-main)
        switch_to_main
        ;;
    --to-solution)
        switch_to_solution
        ;;
    --status)
        show_status
        ;;
    --push-all)
        push_all
        ;;
    --help|"")
        show_help
        ;;
    *)
        echo "❌ Option inconnue: $1"
        echo "Utilisez --help pour voir les options disponibles"
        exit 1
        ;;
esac
