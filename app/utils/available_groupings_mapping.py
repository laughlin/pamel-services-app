from services.groupings_services.nm_groupings import nm_groupings

NM = 'northwestern_medicine'

mappings = {}

mappings[NM] = {}
mappings[NM]['groupings_service'] = nm_groupings

mappings[NM]['v_ga_page'] = {}
mappings[NM]['v_ga_page']['groupings'] = {}
mappings[NM]['v_ga_page']['groupings']['service_lines'] = nm_groupings.service_lines
mappings[NM]['v_ga_page']['groupings']['care_and_conditions'] = nm_groupings.care_and_conditions
mappings[NM]['v_ga_page']['groupings']['regions'] = nm_groupings.regions



