from functools import lru_cache

from pages.code.pages.context_processing import local_link_converter


@lru_cache
def links():
    context = [
        {
            'topic_name': 'Maths',
            'link_data': [
                {'name': 'Index', 'viewname': 'maths:index'},
            ]
        },
        {
            'topic_name': 'Algebra',
            'link_data': [
                {'name': 'Solution of Equations', 'viewname': 'maths:topic_page',
                 'args': ['algebra', 'solution_of_equations']},
                {'name': 'Inequalities', 'viewname': 'maths:topic_page', 'args': ['algebra', 'inequalities']},
                {'name': 'Surds', 'viewname': 'maths:topic_page', 'args': ['algebra', 'surds']},
                {'name': 'Proportions', 'viewname': 'maths:topic_page', 'args': ['algebra', 'proportions']},
                {'name': 'Partial Fractions', 'viewname': 'maths:topic_page', 'args': ['algebra', 'partial_fractions']},
                {'name': 'Rational Expressions', 'viewname': 'maths:topic_page',
                 'args': ['algebra', 'rational_expressions']},
            ]
        },
        {
            'topic_name': 'Calculus',
            'link_data': [
                {'name': 'Basic Differentiation', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'basic_differentiation']},
                {'name': 'Differentiation of Functions', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'differentiation_of_functions']},
                {'name': 'Chain Rule', 'viewname': 'maths:topic_page', 'args': ['calculus', 'chain_rule']},
                {'name': 'Product Rule', 'viewname': 'maths:topic_page', 'args': ['calculus', 'product_rule']},
                {'name': 'Quotient Rule', 'viewname': 'maths:topic_page', 'args': ['calculus', 'quotient_rule']},
                {'name': 'Implicit Differentiation', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'implicit_differentiation']},
                {'name': 'Applications of Differentials', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'applications_of_differentials']},
                {'name': 'Basic Integration', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'basic_integration']},
                {'name': 'Integration as Reverse of Differentiation', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'integration_as_reverse']},
                {'name': 'Integration by Substitution', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'integration_by_substitution']},
                {'name': 'Integration by Parts', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'integration_by_parts']},
                {'name': 'Integrating Partial Fraction', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'integrating_partial_fraction']},
                {'name': 'Differential Equations', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'differential_equations']},
                {'name': 'Integrating Factor Method', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'integrating_factor_method']},
                {'name': 'Simple Harmonic Motion', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'simple_harmonic_motion']},
                {'name': 'Dampened Oscillations', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'dampened_oscillations']},
                {'name': 'Simultaneous Differential Equations', 'viewname': 'maths:topic_page',
                 'args': ['calculus', 'simultaneous_differential_equations']},
            ]
        },
        {
            'topic_name': 'Coordinate Geometry',
            'link_data': [
                {'name': 'Linear Equations', 'viewname': 'maths:topic_page',
                 'args': ['coordinate_geometry', 'linear_equations']},
                {'name': 'Curves', 'viewname': 'maths:topic_page', 'args': ['coordinate_geometry', 'curves']},
                {'name': 'Parametric Equations', 'viewname': 'maths:topic_page',
                 'args': ['coordinate_geometry', 'parametric_equations']},
            ]
        },
        {
            'topic_name': 'Exponential and Logarithms',
            'link_data': [
                {'name': 'Rules', 'viewname': 'maths:topic_page', 'args': ['exponential_and_logarithms', 'rules']},
                {'name': 'Euler\'s Constant and Natural Log', 'viewname': 'maths:topic_page',
                 'args': ['exponential_and_logarithms', 'eulers_constant']},
                {'name': 'Exponential Growth and Decay', 'viewname': 'maths:topic_page',
                 'args': ['exponential_and_logarithms', 'exponential_growth_and_decay']},
            ]
        },
        {
            'topic_name': 'Functions',
            'link_data': [
                {'name': 'Syntax', 'viewname': 'maths:topic_page', 'args': ['functions', 'syntax']},
                {'name': 'Exponentials', 'viewname': 'maths:topic_page', 'args': ['functions', 'exponentials']},
                {'name': 'Modulus', 'viewname': 'maths:topic_page', 'args': ['functions', 'modulus']},
                {'name': 'Modelling', 'viewname': 'maths:topic_page', 'args': ['functions', 'modelling']},
            ]
        },
        {
            'topic_name': 'Graphs',
            'link_data': [
                {'name': 'Sketching Graphs', 'viewname': 'maths:topic_page', 'args': ['graphs', 'sketching_graphs']},
                {'name': 'Transformations', 'viewname': 'maths:topic_page', 'args': ['graphs', 'transformations']},
            ]
        },
        {
            'topic_name': 'Numerical Methods',
            'link_data': [
                {'name': 'Solution of Equations', 'viewname': 'maths:topic_page',
                 'args': ['numerical_methods', 'solution_of_equations']},
                {'name': 'Integration', 'viewname': 'maths:topic_page', 'args': ['numerical_methods', 'integration']},
            ]
        },
        {
            'topic_name': 'Proofs',
            'link_data': [
                {'name': 'Types of Proofs', 'viewname': 'maths:topic_page', 'args': ['proofs', 'types_of_proofs']},
                {'name': 'Proof by Induction', 'viewname': 'maths:topic_page', 'args': ['proof', 'proof_by_induction']},
            ]
        },
        {
            'topic_name': 'Sequences and Series',
            'link_data': [
                {'name': 'Binomial Expansion', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'binomial_expansion']},
                {'name': 'Nth Term and Recurrence Relation', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'nth_term_and_recurrence_relation']},
                {'name': 'Arithmetic Sequences', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'arithmetic_sequences']},
                {'name': 'Geometric Sequences', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'geometric_sequences']},
                {'name': 'Convergent and Divergent', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'convergent_and_divergent']},
                {'name': 'Summation Series', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'summation_series']},
                {'name': 'Maclaurin Series', 'viewname': 'maths:topic_page',
                 'args': ['sequences_and_series', 'maclaurin_series']},

            ]
        },
        {
            'topic_name': 'Trigonometry',
            'link_data': [
                {'name': 'Area & Sine and Cosine Rule', 'viewname': 'maths:topic_page',
                 'args': ['trigonometry', 'area_sine_and_cosine_rule']},
                {'name': 'Sine, Cosine and Tangent Squared', 'viewname': 'maths:topic_page',
                 'args': ['trigonometry', 'sine_cosine_and_tangent_squared']},
                {'name': 'Secant, Cosecant and Cotangent', 'viewname': 'maths:topic_page',
                 'args': ['trigonometry', 'secant_cosecant_and_cotangent']},
                {'name': 'Compound Angle Formula', 'viewname': 'maths:topic_page',
                 'args': ['trigonometry', 'compound_angle_formula']},
            ]
        },
        {
            'topic_name': 'Vectors',
            'link_data': [
                {'name': 'Basic Vectors', 'viewname': 'maths:topic_page', 'args': ['vectors', 'basic_vectors']},
                {'name': 'Dot Product and Cross Product', 'viewname': 'maths:topic_page',
                 'args': ['vectors', 'dot_product_and_cross_product']},
            ]
        },
        {
            'topic_name': 'Data Presentation and Interpretation',
            'link_data': [
                {'name': 'Single Variable Presentation', 'viewname': 'maths:topic_page',
                 'args': ['data_presentation_and_interpretation', 'single_variable_presentation']},
                {'name': 'Bivariate Presentation', 'viewname': 'maths:topic_page',
                 'args': ['data_presentation_and_interpretation', 'bivariate_presentation']},
                {'name': 'Metrics of Data', 'viewname': 'maths:topic_page',
                 'args': ['data_presentation_and_interpretation', 'metrics_of_data']},
            ]
        },
        {
            'topic_name': 'Probability',
            'link_data': [
                {'name': 'Syntax', 'viewname': 'maths:topic_page', 'args': ['probability', 'syntax']},
                {'name': 'Basic Probability', 'viewname': 'maths:topic_page',
                 'args': ['probability', 'basic_probability']},
                {'name': 'Distributions', 'viewname': 'maths:topic_page', 'args': ['probability', 'distributions']},
            ]
        },
        {
            'topic_name': 'Sampling',
            'link_data': [
                {'name': 'Sampling Techniques', 'viewname': 'maths:topic_page',
                 'args': ['sampling', 'sampling_techniques']},
            ]
        },
        {
            'topic_name': 'Statistical Hypothesis Testing',
            'link_data': [
                {'name': 'Syntax', 'viewname': 'maths:topic_page',
                 'args': ['statistical_hypothesis_testing', 'syntax']},
                {'name': 'One and Two Tail Tests', 'viewname': 'maths:topic_page',
                 'args': ['statistical_hypothesis_testing', 'one_and_two_tail_tests']},
                {'name': 'Binomial Probability Hypothesis Testing', 'viewname': 'maths:topic_page',
                 'args': ['statistical_hypothesis_testing', 'binomial_probability_hypothesis_testing']},
                {'name': 'Normal Distribution Hypothesis Testing', 'viewname': 'maths:topic_page',
                 'args': ['statistical_hypothesis_testing', 'normal_distribution_hypothesis_testing']},
                {'name': 'Correlation Hypothesis Testing', 'viewname': 'maths:topic_page',
                 'args': ['statistical_hypothesis_testing', 'correlation_hypothesis_testing']},
            ]
        },
        {
            'topic_name': 'Forces',
            'link_data': [
                {'name': 'Newton\'s Three Laws', 'viewname': 'maths:topic_page',
                 'args': ['forces', 'newtons_three_laws']},
                {'name': 'Vector Treatment of Forces', 'viewname': 'maths:topic_page',
                 'args': ['forces', 'vector_treatment_of_forces']},
                {'name': 'Friction and Normal Contact Force', 'viewname': 'maths:topic_page',
                 'args': ['forces', 'friction_and_normal_contact_force']},
                {'name': 'Connected Particles', 'viewname': 'maths:topic_page',
                 'args': ['forces', 'connected_particles']},
            ]
        },
        {
            'topic_name': 'Kinematics',
            'link_data': [
                {'name': 'Constant Acceleration Kinematics', 'viewname': 'maths:topic_page',
                 'args': ['kinematics', 'constant_acceleration_kinematics']},
                {'name': 'Calculus in Kinematics', 'viewname': 'maths:topic_page',
                 'args': ['kinematics', 'calculus_in_kinematics']},
                {'name': 'Two Dimensional Kinematics', 'viewname': 'maths:topic_page',
                 'args': ['kinematics', 'two_dimensional_kinematics']},
            ]
        },
        {
            'topic_name': 'Rigid Bodies',
            'link_data': [
                {'name': 'Rigid Bodies in Equilibrium', 'viewname': 'maths:topic_page',
                 'args': ['rigid_bodies', 'rigid_bodies_in_equilibrium']},
            ]
        },
        {
            'topic_name': 'Complex Numbers',
            'link_data': [
                {'name': 'Syntax', 'viewname': 'maths:topic_page', 'args': ['complex_numbers', 'syntax']},
                {'name': 'Polynomial Equations', 'viewname': 'maths:topic_page',
                 'args': ['complex_numbers', 'polynomial_equations']},
                {'name': 'Modulus and Argument Form', 'viewname': 'maths:topic_page',
                 'args': ['complex_numbers', 'modulus_and_argument_form']},
                {'name': 'Loci', 'viewname': 'maths:topic_page', 'args': ['complex_numbers', 'loci']},
                {'name': 'De Moivre\'s Theorem', 'viewname': 'maths:topic_page',
                 'args': ['complex_numbers', 'de_moivres_theorem']},
                {'name': 'Nth Roots of a Complex Number', 'viewname': 'maths:topic_page',
                 'args': ['complex_numbers', 'nth_roots_of_a_complex_number']},
                {'name': 'Complex Numbers in Geometry', 'viewname': 'maths:topic_page',
                 'args': ['complex_numbers', 'complex_numbers_in_geometry']},
            ]
        },
        {
            'topic_name': '3D Space',
            'link_data': [
                {'name': 'Planes', 'viewname': 'maths:topic_page', 'args': ['d_space', 'planes']},
                {'name': 'Intersection of Planes', 'viewname': 'maths:topic_page',
                 'args': ['d_space', 'intersection_of_planes']},
                {'name': 'Lines', 'viewname': 'maths:topic_page', 'args': ['d_space', 'lines']},
                {'name': 'Points, Lines and Planes', 'viewname': 'maths:topic_page',
                 'args': ['d_space', 'points_lines_and_planes']},
            ]
        },
        {
            'topic_name': 'Dimensional Analysis',
            'link_data': [
                {'name': 'Dimensional Consistency', 'viewname': 'maths:topic_page',
                 'args': ['dimensional_analysis', 'dimensional_consistency']},
                {'name': 'Modelling with Dimensional Analysis', 'viewname': 'maths:topic_page',
                 'args': ['dimensional_analysis', 'modelling_with_dimensional_analysis']},
            ]
        },
    ]
    return {'maths_links': local_link_converter(context)}


def maths_links(request):
    return links()
