from functools import lru_cache

# noinspection PyUnresolvedReferences
from pages.code.pages.context_processing import local_link_converter


@lru_cache
def links():
    context = [
        {
            'topic_name': 'Physics',
            'link_data':
                [
                    {'name': 'Index', 'viewname': 'physics:index'},

                ]
        },
        {
            'topic_name': 'Measures and Their Errors',
            'link_data': [
                {'name': 'Physical Quantities and Measurements', 'viewname': 'physics:topic_page',
                 'args': ['measures_and_their_errors', 'physical_quantities_and_measurements']},
                {'name': 'SI Units and Prefixes', 'viewname': 'physics:topic_page',
                 'args': ['measures_and_their_errors', 'si_units_and_prefixes']},
            ]
        },
        {
            'topic_name': 'Particles and Radiation',
            'link_data': [
                {'name': 'Particle Classification', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'particle_classification']},
                {'name': 'Conservation Laws', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'conservation_laws']},
                {'name': 'Particles and Antiparticles', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'particles_and_antiparticles']},
                {'name': 'Constituents of the Atom', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'constituents_of_the_atom']},
                {'name': 'Quarks and Antiquarks', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'quarks_and_antiquarks']},
                {'name': 'Particle Interaction', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'particle_interaction']},
                {'name': 'Atom vs Electron', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'atom_vs_electron']},
                {'name': 'Stable and Unstable Nuclei', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'stable_and_unstable_nuclei']},
                {'name': 'Electromagnetic Radiation', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'electromagnetic_radiation']},
                {'name': 'Wave Particle Duality', 'viewname': 'physics:topic_page',
                 'args': ['particles_and_radiation', 'wave_particle_duality']},
            ]
        },
        {
            'topic_name': 'Waves',
            'link_data': [
                {'name': 'Diffraction vs Refraction', 'viewname': 'physics:topic_page',
                 'args': ['waves', 'diffraction_vs_refraction']},
                {'name': 'Interference', 'viewname': 'physics:topic_page', 'args': ['waves', 'interference']},
                {'name': 'Longitudinal and Transverse Waves', 'viewname': 'physics:topic_page',
                 'args': ['waves', 'longitudinal_and_transverse_waves']},
                {'name': 'Progressive Waves, Stationary Waves and Superposition', 'viewname': 'physics:topic_page',
                 'args': ['waves', 'progressive_waves_stationary_waves_and_superposition']},
            ]
        },
        {
            'topic_name': 'Mechanics and Materials',
            'link_data': [
                {'name': 'Work, Energy, Power', 'viewname': 'physics:topic_page',
                 'args': ['mechanics_and_materials', 'work_energy_power']},
                {'name': 'Momentum', 'viewname': 'physics:topic_page', 'args': ['mechanics_and_materials', 'momentum']},
                {'name': 'Moments', 'viewname': 'physics:topic_page', 'args': ['mechanics_and_materials', 'moments']},
                {'name': 'Newtons Laws of Motion', 'viewname': 'physics:topic_page',
                 'args': ['mechanics_and_materials', 'newtons_laws_of_motion']},
                {'name': 'Motion and Force', 'viewname': 'physics:topic_page',
                 'args': ['mechanics_and_materials', 'motion_and_force']},
                {'name': 'Motion and Projectiles', 'viewname': 'physics:topic_page',
                 'args': ['mechanics_and_materials', 'motion_and_projectiles']},
                {'name': 'Young\'s Modulus', 'viewname': 'physics:topic_page',
                 'args': ['mechanics_and_materials', 'youngs_modulus']},
            ]
        },
        {
            'topic_name': 'Electricity',
            'link_data': [
                {'name': 'Circuits', 'viewname': 'physics:topic_page', 'args': ['electricity', 'circuits']},
                {'name': 'Current', 'viewname': 'physics:topic_page', 'args': ['electricity', 'current']},
                {'name': 'Voltage', 'viewname': 'physics:topic_page', 'args': ['electricity', 'voltage']},
                {'name': 'Resistance', 'viewname': 'physics:topic_page', 'args': ['electricity', 'resistance']},
                {'name': 'Cells', 'viewname': 'physics:topic_page', 'args': ['electricity', 'cells']},
            ]
        },
        {
            'topic_name': 'Further Mechanics',
            'link_data': [
                {'name': 'Simple Harmonic Motion', 'viewname': 'physics:topic_page',
                 'args': ['further_mechanics', 'simple_harmonic_motion']},
                {'name': 'Circular Motion', 'viewname': 'physics:topic_page',
                 'args': ['further_mechanics', 'circular_motion']},
                {'name': 'Resonance and Forced Vibrations', 'viewname': 'physics:topic_page',
                 'args': ['further_mechanics', 'resonance_and_forced_vibrations']},
                {'name': 'Periodic Motion', 'viewname': 'physics:topic_page',
                 'args': ['further_mechanics', 'periodic_motion']},
            ]
        },
        {
            'topic_name': 'Thermal Physics',
            'link_data': [
                {'name': 'Ideal Gases', 'viewname': 'physics:topic_page', 'args': ['thermal_physics', 'ideal_gases']},
                {'name': 'Molecular Kinetic Theory', 'viewname': 'physics:topic_page',
                 'args': ['thermal_physics', 'molecular_kinetic_theory']},
                {'name': 'Thermal Energy Transfer', 'viewname': 'physics:topic_page',
                 'args': ['thermal_physics', 'thermal_energy_transfer']},
            ]
        },
        {
            'topic_name': 'Fields and Their Consequences',
            'link_data': [
                {'name': 'Transformers', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'transformers']},
                {'name': 'Capacitance', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'capacitance']},
                {'name': 'Capacitors', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'capacitors']},
                {'name': 'Electromagnetic Induction', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'electromagnetic_induction']},
                {'name': 'Electric Fields', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'electric_fields']},
                {'name': 'Electric Potential', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'electric_potential']},
                {'name': 'Magnetic Fields', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'magnetic_fields']},
                {'name': 'Magnetic Flux', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'magnetic_flux']},
                {'name': 'Gravitational Fields', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'gravitational_fields']},
                {'name': 'Gravitational Potential', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'gravitational_potential']},
                {'name': 'Orbits', 'viewname': 'physics:topic_page',
                 'args': ['fields_and_their_consequences', 'orbits']},
            ]
        },
        {
            'topic_name': 'Nuclear Physics',
            'link_data':
                [
                    {'name': 'Alpha, Beta and Gamma Radiation', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'alpha_beta_and_gamma_radiation']},
                    {'name': 'Induced Fission', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'induced_fission']},
                    {'name': 'Mass and Energy', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'mass_and_energy']},
                    {'name': 'Nuclear Instability and Radius', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'nuclear_instability_and_radius']},
                    {'name': 'Radioactive Decay', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'radioactive_decay']},
                    {'name': 'Rutherford Scattering', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'rutherford_scattering']},
                    {'name': 'Nuclear Safety', 'viewname': 'physics:topic_page',
                     'args': ['nuclear_physics', 'nuclear_safety']},
                ]
        },
        {
            'topic_name': 'Practical Skills',
            'link_data':
                [
                    {'name': 'Stationary Waves on a String', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'stationary_waves_on_a_string']},
                    {'name': 'Interference Effects', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'interference_effects']},
                    {'name': 'Determination of g', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'determination_of_g']},
                    {'name': 'Determination of Young\'s Modulus', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'determination_of_youngs_modulus']},
                    {'name': 'Determination of Resistivity of a Wire', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'determination_of_resistivity_of_a_wire']},
                    {'name': 'Internal Resistance and emf', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'internal_resistance_and_emf']},
                    {'name': 'Simple Harmonic Motion', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'simple_harmonic_motion']},
                    {'name': 'Boyle\'s and Charles\' Laws', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'boyles_and_charles_laws']},
                    {'name': 'Charging and Discharging Capacitors', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'charging_and_discharging_capacitors']},
                    {'name': 'Magnetic Force on a Wire', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'magnetic_force_on_a_wire']},
                    {'name': 'Magnetic Flux Linkage', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'magnetic_flux_linkage']},
                    {'name': 'Inverse Square Law for Gamma Radiation', 'viewname': 'physics:topic_page',
                     'args': ['practical_skills', 'inverse_square_law_for_gamma_radiation']},
                ]
        },
    ]
    return {'physics_links': local_link_converter(context)}


def physics_links(request):
    return links()
